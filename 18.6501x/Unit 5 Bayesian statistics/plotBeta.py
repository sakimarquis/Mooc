# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:39:19 2019

@author: saki
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plotBeta(paras, figsize = (15,3)):
    """
    input: pairs of parameters of Beta distribution
    output: plot
    """
    n = len(paras)
    f,ax=plt.subplots(1,n, figsize = figsize)
    i = 0
    for a,b in paras:
        ax[i].plot(np.linspace(0,1),stats.beta.pdf(np.linspace(0,1), a=a, b=b))
        ax[i].set_title("alpha="+ str(a) + ", beta=" + str(b))
        ax[i].set_xlabel(r'$x$')
        i+=1
    ax[0].set_ylabel(r'Beta$(\alpha,\beta, x)$')
 
    
paras = [[0.5,0.5],[1,1],[1,2],[2,1]]
plotBeta(paras)


paras2 = [[0.6,0.1],[0.5,1],[1,0.5],[1,1],[2,10]]
plotBeta(paras2)