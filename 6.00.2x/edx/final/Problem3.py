# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:07:45 2018

@author: Saki
"""

# =============================================================================
# Problem 3
# =============================================================================

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    BUCKET = ["Red"] * 4 + ["Green"] * 4
    count = 0
    for trial in range(numTrials):
        rand_bucket = BUCKET[::]
        random.shuffle(rand_bucket)
        first = rand_bucket.pop(0)
        second = rand_bucket.pop(0)
        third = rand_bucket.pop(0)
        if first == second and first == third:
            count += 1
    return count / numTrials