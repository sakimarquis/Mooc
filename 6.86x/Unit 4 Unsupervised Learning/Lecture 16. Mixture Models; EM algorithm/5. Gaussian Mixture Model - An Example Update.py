# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:12:44 2019

@author: saki
"""

from scipy import stats


# =============================================================================
# 注意，这里的变量名的prior和posterior不是这个意思！！！！
# 我最开始理解错了含义，根本没有贝叶斯在里面！
# 为了方便，我不修改变量名
# 在这里，prior的意思是weight，posterior的意思是assignment
# =============================================================================

mu1 = -3
mu2 = 2
sigma1 = 2
sigma2 = 2
prior1 = 0.5
prior2 = 0.5
x = [0.2, -0.9, -1, 1.2, 1.8]

cluster1 = stats.norm(loc = mu1, scale = sigma1)
cluster2 = stats.norm(loc = mu2, scale = sigma2)

# =============================================================================
# E-Step
# =============================================================================

posterior1 = prior1 * cluster1.pdf(x) / (prior1 * cluster1.pdf(x) + prior2 * cluster2.pdf(x))
posterior2 = prior2 * cluster2.pdf(x) / (prior1 * cluster1.pdf(x) + prior2 * cluster2.pdf(x))

# =============================================================================
# M-Step
# =============================================================================

n1 = sum(posterior1)
n2 = sum(posterior2)
new_prior1 = n1 / len(x)
new_prior2 = n2 / len(x)
new_mu1 = sum(posterior1 * x) / n1
new_mu2 = sum(posterior2 * x) / n2
new_sigma1 = sum(posterior1 * (x - new_mu1) ** 2) / n1
new_sigma2 = sum(posterior2 * (x - new_mu2) ** 2) / n2

