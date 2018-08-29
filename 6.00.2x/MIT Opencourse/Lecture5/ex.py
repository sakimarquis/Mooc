# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 22:53:18 2018

@author: Saki
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randint(0, 49)*2

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10
    
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randint(5, 10)*2