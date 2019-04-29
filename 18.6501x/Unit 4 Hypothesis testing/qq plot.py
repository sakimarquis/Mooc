# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:04:30 2019

@author: saki
"""

import numpy as np
import scipy
import statsmodels as sm
import math
import matplotlib as plt

# 2. KS and KL Tests - QQ Plot
S = [0.28, 0.2, 0.01, 0.80, 0.1]
S.sort()
# qqplot S against Uniform(0,1)
sm.qqplot(np.array(S), dist=scipy.stats.uniform, loc = 0, scale = 1, line='45')


# 3. QQ Plots
sim_size = 1000

standardnorm_rv = np.random.normal(loc = 0, scale = 1, size = sim_size)
sm.qqplot(standardnorm_rv, line='45')

laplace_rv = scipy.stats.laplace.rvs(loc = 0, scale = math.sqrt(2) ,size = sim_size)
sm.qqplot(laplace_rv, line='45')

cauchy_rv = scipy.stats.cauchy.rvs(size = sim_size)
sm.qqplot(cauchy_rv, line='45')

exp_rv = scipy.stats.expon.rvs(loc = 0, scale = 1, size = sim_size)
sm.qqplot(exp_rv, line='45')

unif_rv = scipy.stats.uniform.rvs(loc = -1*math.sqrt(3), scale = 2*math.sqrt(3), size = sim_size)
sm.qqplot(unif_rv, line='45')

