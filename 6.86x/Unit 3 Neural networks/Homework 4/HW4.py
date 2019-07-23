# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:24:48 2019

@author: saki
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. Neural Networks
# 1.1 Feed Forward Step
# =============================================================================

W = np.array([[1, 0, -1], [0, 1, -1], [-1, 0, -1], [0, -1, -1]])
V = np.array([[1, 1, 1, 1, 0], [-1, -1, -1, -1, 2]])
X_input = np.array([3, 14, 1])

Z = W @ X_input
Z[Z < 0] = 0
U = V @ np.hstack([Z, 1])
U[U < 0] = 0

# =============================================================================
# 1.2 Decision Boundaries
# =============================================================================

# four lines: x=1,x=-1,y=1,y=-1
x = np.linspace(-2,2,10)
y = np.ones(10)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(y, x)
ax.plot(x, -y)
ax.plot(-y, x)


# =============================================================================
# 2. LSTM
# 2.1 states
# =============================================================================

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def input_gate(h, x):
    W_ih = 0
    W_ix = 100
    b_i = 100
    return round(sigmoid(W_ih * h + W_ix * x + b_i))


def forget_gate(h, x):
    W_fh = 0
    W_fx = 0
    b_f = -100
    return round(sigmoid(W_fh * h + W_fx * x + b_f))


def output_gate(h, x):
    W_oh = 0
    W_ox = 100
    b_o = 0
    return round(sigmoid(W_oh * h + W_ox * x + b_o))


def memory_cell(h, x, c):
    W_ch = -100
    W_cx = 50
    b_c = 0
    ipt = input_gate(h, x) * round(np.tanh(W_ch * h + W_cx * x + b_c))
    forget = forget_gate(h, x) * c
    return ipt + forget


def visible(h, x, c):
    return output_gate(h, x) * round(np.tanh(c))


def lstm_states(x):
    h = [0]
    c = [0]
    for i in range(len(x)):
        c.append(memory_cell(h[-1], x[i], c[-1]))
        h.append(visible(h[-1], x[i], c[-1]))
    return h, c


X1 = [0, 0, 1, 1, 1, 0]
X2 = [1, 1, 0, 1, 1]
print(lstm_states(X1)[0][1:])
print(lstm_states(X2)[0][1:])