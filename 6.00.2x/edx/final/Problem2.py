# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:07:25 2018

@author: Saki
"""

# =============================================================================
# Problem 2
# =============================================================================

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals


pylab.plot([i for i in range(1000)], xVals, 'r') 
pylab.plot([i for i in range(1000)], tVals, 'r') 

pylab.plot(xVals, zVals)
pylab.plot(xVals, yVals)
pylab.plot(xVals, sorted(yVals))
pylab.plot(sorted(xVals), yVals)
pylab.plot(sorted(xVals), sorted(yVals))