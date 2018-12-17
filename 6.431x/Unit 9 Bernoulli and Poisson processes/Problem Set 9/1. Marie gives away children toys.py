# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:15:55 2018

@author: Saki
"""

p = 3/4
q = 1/3


Q1 = (1 - p*q)**2
print(Q1)

Q2 = (1 - p*q)**3 * p*q
print(Q2)


Q3 = (1 - p*q)**2 * p*q
print(Q3)

Q4 = 3 * (1-p*q)**2 * p*q * p*q
print(Q4)

a = (1-p*q)**3 #前三个一个都没给的概率
b = 3 * (1-p*q)**2 * p*q#前三个给了一个的概率
Q5 = a/(a+b) * (p*q)**2 + b/(a+b) * (1-p*q)*p*q #前三个一个都没给或者给了一个
print(Q5)

Q6 = 1 - 4 * (p*q)**3 * (1-p*q) #1-前四个全送了
print(Q6)

exp = 6/(p*q) #带6个娃娃全送走需要的拜访次数期望
Q7 = exp * (1-p) * q
print(Q7)
