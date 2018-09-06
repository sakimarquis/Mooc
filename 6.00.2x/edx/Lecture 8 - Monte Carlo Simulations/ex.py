# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:30:00 2018

@author: Saki
"""
# =============================================================================
# ex5
# =============================================================================
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    count = 0
    for i in range(numTrials):
        bucket = ['Red'] * 3 + ['Green'] * 3
        random.shuffle(bucket)
        first = bucket.pop(0)
        second = bucket.pop(0)
        third = bucket.pop(0)
        if first == second and first == third:
            count += 1
    return count/numTrials