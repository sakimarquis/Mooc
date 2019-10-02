# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:09:46 2019

@author: saki
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1
# =============================================================================

p = 0.1

def info_entropy(p_arr):
    entropy = 0
    for p in p_arr:
        entropy += (-p * np.log2(p))
    return entropy

total_entropy = info_entropy([p, 1 - p])


# =============================================================================
# 2
# =============================================================================

spike_pos = 1/2
spike_neg = 1/18
p_spike = p * spike_pos + (1 - p) * spike_neg
p_notspike = p * (1 - spike_pos) + (1 - p) * (1 - spike_neg)
noise_entropy = info_entropy([p_spike, p_notspike])
MI = total_entropy - noise_entropy


# =============================================================================
# 7.
# =============================================================================

TIME = 10

with open('tuning.pickle', 'rb') as f:
    data = pickle.load(f)

n1 = data['neuron1']
n2 = data['neuron2']
n3 = data['neuron3']
n4 = data['neuron4']
stim = data['stim']


plt.plot(stim, n1.mean(axis = 0))
plt.xlabel('Stimulus')
plt.ylabel('Firing rate ')
plt.title('Tuning Function')
plt.show()

# =============================================================================
# 8, 10s, 100 trials, 24 stimlus
# =============================================================================

def fano(neuron):
    fano_list = []
    for i in range(neuron.shape[1]):
        firing_rate = neuron[:,i]
        spike = firing_rate * TIME
        fano_list.append(spike.var() / spike.mean())
    return fano_list

print(fano(n1))
print(fano(n3))

# =============================================================================
# 9, 10 trials of 10 seconds
# =============================================================================

with open('pop_coding.pickle', 'rb') as f:
    pop_data = pickle.load(f)

r1 = pop_data['r1']
r2 = pop_data['r2']
r3 = pop_data['r3']
r4 = pop_data['r4']
c1 = pop_data['c1']
c2 = pop_data['c2']
c3 = pop_data['c3']
c4 = pop_data['c4']

r1_max = n1.mean(axis = 0).max()
r2_max = n2.mean(axis = 0).max()
r3_max = n3.mean(axis = 0).max()
r4_max = n4.mean(axis = 0).max()

v_pop1 = ((r1.mean() - 0) / r1_max) * c1
v_pop2 = ((r2.mean() - 0) / r2_max) * c2
v_pop3 = ((r3.mean() - 0) / r3_max) * c3
v_pop4 = ((r4.mean() - 0) / r4_max) * c4
v_pop = v_pop1 + v_pop2 + v_pop3 + v_pop4
x, y = v_pop
theta = (np.arctan(y/x) / (2 * np.pi) * 360) % 360

print(int(360 - theta + 90))

