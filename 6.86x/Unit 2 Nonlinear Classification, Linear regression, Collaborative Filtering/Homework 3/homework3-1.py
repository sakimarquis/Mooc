# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:26:31 2019

@author: saki
"""

import numpy as np

# =============================================================================
# 1. (a) (b)
# =============================================================================

k = 1
L = 1
u_0 = np.array([6,0,3,6]).reshape(4,1)
v_0 = np.array([4,2,1]).reshape(3,1)

print(u_0 @ v_0.T)


print(1/2*(19**2 + 4 + 1 + 64 + 81 + 0))
regul_term = 1/2*(np.linalg.norm(u_0))**2 + 1/2*(np.linalg.norm(v_0))**2
print(regul_term)

# =============================================================================
# #
# # 1. (c)
# # this part must use sage
# # 
# =============================================================================
# 
# var('u1,u2,u3,u4,v1,v2,v3')
# (u1, u2, u3, u4, v1, v2, v3)
# U = matrix([u1,u2,u3,u4]).transpose()
# V = matrix([v1,v2,v3]).transpose()
# X = U * V.transpose()
# J1 = 1/2*((5-X[0,0])^2+(7-X[0,2])^2+(2-X[1,1])^2+(4-X[2,0])^2+(3-X[3,1])^2+(6-X[3,2])^2)
# J2 = 1/2*((U[0,0]^2+U[1,0]^2+U[2,0]^2+U[3,0]^2+V[0,0]^2+V[1,0]^2+V[2,0]^2))
# J = J1+J2
# equ1 = (derivative(J,u1) == 0)
# equ2 = (derivative(J,u2) == 0)
# equ3 = (derivative(J,u3) == 0)
# equ4 = (derivative(J,u4) == 0)
# # To get numerical answers do substitutions, like that
# equ1.substitute(v1=4,v2=2,v3=1)
# # even better
# solve(equ1.substitute(v1=4,v2=2,v3=1),u1)
# =============================================================================
