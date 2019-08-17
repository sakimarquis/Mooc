import numpy as np
import em
import common


# =============================================================================
# 7. Implementing EM for matrix completion
# =============================================================================

X = np.loadtxt("test_incomplete.txt")
X_gold = np.loadtxt("test_complete.txt")

K = 4
n, d = X.shape
seed = 0

# for incomplete case
mixture, post = common.init(X, K = K, seed = seed)
post, log_likelihood = em.estep(X, mixture)
mixture = em.mstep(X, post, mixture)


# =============================================================================
# 8. Using the mixture model for collaborative filtering
# Reporting log likelihood values on Netflix data
# =============================================================================

X = np.loadtxt("netflix_incomplete.txt")

mixture, post = common.init(X, K = 1, seed = 0)
post, log_likelihood = em.estep(X, mixture)
mixtured = em.mstep(X, post, mixture)


Ks = [1, 12]
seeds = [0, 1, 2, 3, 4]

for K in Ks:
    for seed in seeds:
        mixture, post = common.init(X, K = K, seed = seed)
        mixture, post, log_likelihood = em.run(X, mixture, post)
        print(K, seed, log_likelihood)


# =============================================================================
# Completing missing entries
# =============================================================================

X = np.loadtxt("test_incomplete.txt")
X_gold = np.loadtxt("test_complete.txt")

mixture, post = common.init(X, K = 4, seed = 0)
mixture, post, log_likelihood = em.run(X, mixture, post)
X_pred = em.fill_matrix(X, mixture)
RMSE = common.rmse(X_gold, X_pred)
print(X_pred, RMSE)


# =============================================================================
# Comparing with gold targets
# =============================================================================

X = np.loadtxt("netflix_incomplete.txt")
X_gold = np.loadtxt('netflix_complete.txt')

mixture, post = common.init(X, K = 12, seed = 1)
mixture, post, log_likelihood = em.run(X, mixture, post)
X_pred = em.fill_matrix(X, mixture)
RMSE = common.rmse(X_gold, X_pred)
print(RMSE)
