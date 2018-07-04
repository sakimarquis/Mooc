# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:07:33 2018

@author: Saki
"""

chance_of_tornado = 0.01

#离散分布
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
    
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
    if tornado_events[j]==1 and tornado_events[j-1]==1:
        two_days_in_a_row+=1
print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))

x = np.random.binomial(2, chance_of_tornado, 1000000)
print((x>=2).sum())