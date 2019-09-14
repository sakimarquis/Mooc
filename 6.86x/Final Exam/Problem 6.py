# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:54:02 2019

@author: saki
"""

import numpy as np

def Relu(vector):
    return np.maximum(0, vector)

def sign(vector):
    v = vector.copy()
    v[v >= 0] = 1
    v[v < 0] = 0
    return v

def hidden(last_state, new_input):
    return Relu(W_ss @ last_state + W_sx @ new_input)

def final(last_state):
    return sign(W_sy @ last_state + W_0)

s_0 = np.array([0, 0]).reshape(2,1)
W_ss = np.array([[-1, 0], [0, 1]])
W_sx = np.array([[1, 0], [0, 1]])

A = np.array([1, 0]).reshape(2,1)
B = np.array([0, 1]).reshape(2,1)


# =============================================================================
# 6. (2)
# =============================================================================

s_1 = hidden(s_0, A)
s_2 = hidden(s_1, A)
print(s_2)

s_1 = hidden(s_0, A)
s_2 = hidden(s_1, B)
s_3 = hidden(s_2, B)
print(s_3)

s_1 = hidden(s_0, B)
s_2 = hidden(s_1, A)
s_3 = hidden(s_2, A)
print(s_3)


# =============================================================================
# 6. (4)
# 下面我都理解错了，我把结果理解成了一个向量而不是一个标量
# =============================================================================

# 1st
s_0 = np.array([0, 0]).reshape(2,1)
W_ss = np.array([[1, 0], [0, 1]])
W_sx = np.array([[1, 0], [0, 1]])
#W_sy = np.array([[1, 0], [0, 1]])
W_sy = np.array([1, 2])
W_0 = 0

s_1 = hidden(s_0, B)
s_2 = hidden(s_1, A)
s_3 = hidden(s_2, A)
s_4 = final(s_3)
print(s_3)
print(s_4)


# 2nd
s_0 = np.array([0, 0]).reshape(2,1)
W_ss = np.array([[1, 0], [0, 1]])
W_sx = -np.array([[1, 0], [0, 1]])
#W_sy = -np.array([[1, 0], [0, 1]])
W_sy = np.array([1, 2])
W_0 = 0

s_1 = hidden(s_0, A)
s_2 = final(s_1)

print(s_1)
print(s_2)


# 3rd
s_0 = np.array([1, 1]).reshape(2,1)
W_ss = np.array([[1, 0], [0, 1]])
W_sx = np.array([[1, 0], [0, 1]])
#W_sy = -np.array([[1, 0], [0, 1]])
W_sy = np.array([1, 2])
W_0 = np.sum(W_sy)

s_1 = hidden(s_0, A)
s_2 = final(s_1)

print(s_1)
print(s_2)


# 4th
s_0 = np.array([1, 1]).reshape(2,1)
W_ss = np.array([[1, 0], [0, 1]])
W_sx = np.array([[1, 0], [0, 1]])
#W_sy = np.array([[1, 0], [0, 1]])
W_sy = np.array([1, 2])
W_0 = -np.sum(W_sy)

s_1 = hidden(s_0, A)
s_2 = final(s_1)
print(s_1)
print(s_2)


s_0 = np.array([1, 1]).reshape(2,1)
W_ss = np.array([[1, 0], [0, 1]])
W_sx = np.array([[1, 0], [0, 1]])
W_sy = np.array([[-1, 0], [0, 1]])
W_0 = -np.sum(W_sy)

s_1 = hidden(s_0, A)
s_2 = hidden(s_1, A)
s_3 = final(s_2)
print(s_2)
print(s_3)


# =============================================================================
# 6. (5)
# =============================================================================

# test case for falsify option 4
s_0 = np.array([0, 0]).reshape(2,1)
W_ss = np.array([[1, 0], [0, 1]])
W_sx = np.array([[1, 0], [0, 1]])
W_sy = np.array([[-2, 3]])
W_0 = 0

s_1 = hidden(s_0, A)
s_2 = hidden(s_1, A)
s_3 = hidden(s_2, B)
s_4 = final(s_3)
print(s_3)
print(s_4)

z = np.array([1, 1])
W_zy = W_sy
print(sign(W_zy @ z))

