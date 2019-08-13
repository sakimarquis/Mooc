import numpy as np
import kmeans
import common
import naive_em
import em
from scipy.stats import multivariate_normal

X = np.loadtxt("toy_data.txt")
Ks = [1, 2, 3, 4]
seeds = [0, 1, 2, 3, 4]


# =============================================================================
# 2. K-means
# =============================================================================

for K in Ks:
    for seed in seeds:
        mixture, post = common.init(X, K, seed = seed) # Initialize K-means
        mixture, post, cost = kmeans.run(X, mixture, post) # K-means
        common.plot(X, mixture, post, [K, seed]) # Plot initialization
        print(cost)


# =============================================================================
# 3. Expectation–maximization algorithm
# =============================================================================

def test_2dgaussian_pdf(X, mu, var):
    y1 = naive_em.pdf_2dgaussian(X, mu, var)
    y2 = multivariate_normal.pdf(X, mean=mu.reshape(2,), cov = var[0])
    return all(y1 - y2) < 1e-6


# 2dgaussian
mixture, post = common.init(X, 1)
mu, var, p = mixture
test_2dgaussian_pdf(X, mu, var)

# E_step
mixture, post = common.init(X, 3, seed=0)
mu, var, p = mixture
post, log_likelihood = naive_em.estep(X, mixture)

# M_step
mixture = naive_em.mstep(X, post)

# RUN
mixture, post = common.init(X, 3, seed=0)
mixture, post, log_likelihood = naive_em.run(X, mixture, post)


# =============================================================================
# 4. Comparing K-means and EM
# =============================================================================

for K in Ks:
    for seed in seeds:
        mixture, post = common.init(X, K = K, seed = seed) # Initialize K-means
        mixture, post, log_likelihood = naive_em.run(X, mixture, post)
        common.plot(X, mixture, post, [K, seed])
        print(K, seed, log_likelihood)


# =============================================================================
# 5. Bayesian Information Criterion
# Picking the best K
# =============================================================================

for K in Ks:
    mixture, post = common.init(X, K = K) # Initialize K-means
    mixture, post, log_likelihood = naive_em.run(X, mixture, post)
    BIC = common.bic(X, mixture, log_likelihood)
    print(K, BIC)

