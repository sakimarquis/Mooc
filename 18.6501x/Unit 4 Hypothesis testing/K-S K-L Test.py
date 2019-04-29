X_n = [0.8, 0.7, 0.4, 0.7, 0.2]

import math
n  = len(X_n)
X_n.sort()
T_n = max([max(abs(i/n-X_n[i]), abs((i+1)/n-X_n[i])) for i in range(0,n)])*math.sqrt(n)


import numpy as np
from scipy import stats as st
x = np.sort(np.array(X_n))
T_n, p_value = st.kstest(x, 'uniform', alternative='less')
T_n = T_n*np.sqrt(len(x))


from statsmodels import stats
T_n = stats.diagnostic.lilliefors(X_n, dist='norm', pvalmethod='approx')