"""Mixture model using EM"""
from typing import Tuple
import numpy as np
from common import GaussianMixture


def pdf_2dgaussian(X, mu, var):
    """
    We assume the simplest multivariate Gaussian model, where all dimensions
    are independent (therefore  cov(xi,xj)=0 ) and has the same variance.

    And Σ = σI, Σ^1/2 = det(σI) = σ^d

    Args:
        X: (n, d) data
        mu: (1, d) mean of a multivariate_gaussian
        var, scalar variance of a multivariate_gaussian

    Returns:
        probability of x in this multivariate_gaussian
    """
    n, d = X.shape
    tiled_mu = np.tile(mu, (n, 1))
    y = 1/np.sqrt((2*np.pi*var)**d) * np.exp(-1/2 * np.einsum("ij -> i",(X - tiled_mu)**2) / var)
    return y


def estep(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step: Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (n, K) array holding the soft counts
            for all components for all examples
        float: log-likelihood of the assignment
    """
    mu, var, weight = mixture
    n, _ = X.shape
    k, _ = mu.shape
    prob_mat = np.zeros([n, k])
    prob_all = np.zeros(n)
    for i in range(k):
        prob = weight[i] * pdf_2dgaussian(X, mu[i], var[i])
        prob_mat[:,i] = prob
        prob_all += prob
    post = prob_mat / np.tile(prob_all.reshape(n, 1), (1, k))
    log_likelihood = np.sum(np.log(np.sum(prob_mat, axis = 1)))
    return post, log_likelihood


def mstep(X: np.ndarray, post: np.ndarray) -> GaussianMixture:
    """M-step: Updates the gaussian mixture by maximizing the log-likelihood
    of the weighted dataset

    Args:
        X: (n, d) array holding the data
        post: (n, K) array holding the soft counts
            for all components for all examples

    Returns:
        GaussianMixture: the new gaussian mixture
    """
    n_data, dim = X.shape
    n_data, k = post.shape
    n_clusters = np.einsum("ij -> j", post)
    weight = n_clusters / n_data
    mu =  post.T @ X / n_clusters.reshape(k, 1)
    var = np.zeros(k)
    for i in range(k):
        var[i] = np.sum(post[:,i].T @ (X - mu[i])**2 / (n_clusters[i] * dim))
    return GaussianMixture(mu, var, weight)


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
        mixture = mstep(X, post)
        if old_log_likelihood is not None:
            if (new_log_likelihood - old_log_likelihood) < 1e-6 * abs(new_log_likelihood):
                break
        old_log_likelihood = new_log_likelihood
    return mixture, post, new_log_likelihood
