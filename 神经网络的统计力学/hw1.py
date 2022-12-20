# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:55:40 2022
hdx@arizona.edu
"""

import numpy as np
import matplotlib.pyplot as plt
# np.random.seed(1)

K = 3   # interaction per Sourlas code 
R = 0.5  # ratio of information strength between and after encoding

N = 15  # number of original binary message
M = int(N / R)  # number of binary message after encoding
p = 0.05  # flipping prob
beta = np.log((1-p)/p)/2  # optimal inverse temperature
num_step = 50

message = np.random.choice([-1, 1], size=N)  # original message

def Sourlas_encoding(message, K, N, M):
    Sourlas_code = np.zeros(M)
    conn_N = [[] for _ in range(N)]  # which connects to a spin
    conn_M = []  # which connects to an interaction
    for i in range(M):
        spins_J_a = np.random.choice(N, size=K, replace=False)  # partial a
        Sourlas_code[i] = np.product(message[spins_J_a])
        
        conn_M.append(spins_J_a)
        for spin in spins_J_a:
            conn_N[spin].append(i)
        
    return Sourlas_code, conn_N, conn_M

Sourlas_code, conn_N, conn_M = Sourlas_encoding(message, K, N, M)
print(Sourlas_code)
print(conn_N)
print(conn_M)


Ja = Sourlas_code * np.random.choice([-1,1],p=(p, 1 - p), size=M) # (2.6)


U_ai = np.random.rand(M, N)
H_ia = np.random.rand(N, M)
m = np.zeros([N])
acc_list = []
for t in range(num_step):
    U_ai_new = np.zeros([M, N])
    H_ia_new = np.zeros([N, M])
    for i in range(N):
        sum_U_bi = np.sum(U_ai[conn_N[i],i])
        for a in conn_N[i]:
            H_ia_new[i,a] = sum_U_bi - U_ai[a,i]
    for a in range(M):
        for i in conn_M[a]:
            prod = 1
            for k in conn_M[a]:
                if k!=i: prod *= np.tanh(beta * H_ia[k, a])
            U_ai_new[a,i] = 1/beta*np.arctanh(np.tanh(beta*Ja[a])*prod)
    U_ai, H_ia = U_ai_new, H_ia_new
    # print('U',U_ai)
    # print('H',H_ia)
    for i in range(N):
        m[i] = np.tanh(np.sum(beta * U_ai[conn_N[i],i]))
    xi_dec = (m>0)*2-1
    acc = np.mean(xi_dec==xi)
    acc_list.append(acc)
    print('step',t, 'm',m,'xi_dec',xi_dec, 'xi', xi, 'correct', acc)
plt.plot(range(num_step), acc_list)
plt.xlabel('Iteration')
plt.ylabel('Accuracy')
plt.show()
