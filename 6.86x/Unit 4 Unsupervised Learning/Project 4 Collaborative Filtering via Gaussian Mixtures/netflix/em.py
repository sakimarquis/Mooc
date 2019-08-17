"""Mixture model for matrix completion"""
from typing import Tuple
import numpy as np
from scipy.special import logsumexp
from common import GaussianMixture


def log_pdf_gaussian(X, mu, var):
    """
    We assume the simplest multivariate Gaussian model, where all dimensions
    are independent (therefore  cov(xi,xj)=0 ) and has the same variance.

    And Σ = σI, Σ^1/2 = det(σI) = σ^d

    Args:
        X: (n, d) data
        mu: (1, d) mean of a multivariate_gaussian
        var, scalar variance of a multivariate_gaussian

    Returns:
        log probability of x in this multivariate_gaussian
    """
    n, _ = X.shape
    tiled_mu = np.tile(mu, (n, 1))
    d = np.sum(1 - X.mask, axis = 1)
    log_y = np.log(1) - d/2 * np.log(2*np.pi*var) - 1/2 * np.einsum("ij -> i", (X - tiled_mu)**2) / var
    return log_y


def estep(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step: Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the assignment

    """
    mu, var, weight = mixture
    n, _ = X.shape
    k, _ = mu.shape
    log_prob_mat = np.zeros([n, k])
    Xm = np.ma.array(X, mask = (X == 0))
    for i in range(k):
        # 通过观察到的点计算在mixture中的位置，找到posterior
        log_prob = np.log(weight[i] + 1e-16) + log_pdf_gaussian(Xm, mu[i], var[i])
        log_prob_mat[:,i] = log_prob
    log_prob_all = logsumexp(log_prob_mat, axis = 1)
    log_post = log_prob_mat - np.tile(log_prob_all.reshape(n, 1), (1, k))
    post = np.exp(log_post)
    log_likelihood = np.sum(log_prob_all)
    return post, log_likelihood


def mstep(X: np.ndarray, post: np.ndarray, mixture: GaussianMixture,
          min_variance: float = .25) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data, with incomplete entries (set to 0)
        post: (n, K) array holding the soft counts
            for all components for all examples
        mixture: the current gaussian mixture
        min_variance: the minimum variance for each gaussian

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    old_mu, dum_var, dum_p = mixture
    n_data, dim = X.shape
    n_data, k = post.shape
    n_clusters = np.einsum("ij -> j", post)
    weight = n_clusters / n_data


    Cu = (X != 0)
    # post.T @ Cu 是整个后验概率中，按照X是否有值，进行叠加
    # 为了numerical instability，本来是mu_update = (post.T @ X) / (post.T @ Cu)
    mu_update = np.exp( np.log(post.T @ X + 1e-16) - np.log(post.T @ Cu + 1e-16) )
    # 因为缺失值缺失的不是整个向量，而是向量中的某个坐标，所以我们确定是不是有理由
    # 进行update的时候，我们要确定的，也是这个一个坐标有没有足够的证据，而不是整个向量
    # if_update = (np.sum(post.T @ Cu, axis = 1) >= 15).reshape(k,1)
    if_update = (post.T @ Cu >= 1)
    mu = mu_update * if_update + old_mu * (1 - if_update)

    var = np.zeros(k)
    for i in range(k):
        var[i] = np.sum(post[:,i].T @ np.where(X > 0, (X - mu[i])**2, 0) / (post.T @ np.sum(Cu, axis = 1))[i])
    return GaussianMixture(mu, np.maximum(var, min_variance), weight)


def run(X: np.ndarray, mixture: GaussianMixture,
        post: np.ndarray) -> Tuple[GaussianMixture, np.ndarray, float]:
    """Runs the mixture model

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the current assignment
    """
    old_log_likelihood = None
    while 1:
        post, new_log_likelihood = estep(X, mixture)
        mixture = mstep(X, post, mixture)
        if old_log_likelihood is not None:
            if (new_log_likelihood - old_log_likelihood) < 1e-6 * abs(new_log_likelihood):
                break
        old_log_likelihood = new_log_likelihood
    return mixture, post, new_log_likelihood



def fill_matrix(X: np.ndarray, mixture: GaussianMixture) -> np.ndarray:
    """Fills an incomplete matrix according to a mixture model

    Args:
        X: (n, d) array of incomplete data (incomplete entries = 0)
        mixture: a mixture of gaussians

    Returns
        np.ndarray: a (n, d) array with completed data
    """
    mu, dum_var, dum_p = mixture
    post, _ = estep(X, mixture)
    x_est = post @ mu # np.sum(post, axis = 1) = 1
    return np.where(X == 0, x_est, X)
