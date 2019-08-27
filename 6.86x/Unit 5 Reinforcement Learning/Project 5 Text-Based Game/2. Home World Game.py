# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 00:42:22 2019

@author: saki
"""


# =============================================================================
# Optimal episodic reward
# =============================================================================

gamma = 0.5
cost = -0.01
reward = 1

# case 1: in the room of the quest, get reward
no_step = gamma**0 * reward
# case 2: 1 step away from room. one step cost + gamma*reward
one_step = cost + gamma**1 * reward
# case 3: 2 steps away from room. one step + gamma * another step cost + gamma^2 * reward
two_step = cost + gamma**1 * cost + gamma**2 * reward

V = (no_step + 2 * one_step + two_step) / 4
print(V)