# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:58:59 2019

@author: saki
"""

import numpy as np

# =============================================================================
# Quiz 2.2: Nernst equation
# Reversal potential
# =============================================================================

K = 1.4e-23 # J/K
T = 300 # K
e = 1.6e-19 # C


def nernst_equation(C_int, C_ext, z):
    """
    return in volt
    """
    E_rev = - K * T / (z * e) * np.log(C_int / C_ext)
    return E_rev

C_int = {}
C_ext = {}
z = {}
C_int['K'] = 140
C_ext['K'] = 5
z['K'] = 1
C_int['Na'] = 10
C_ext['Na'] = 145
z['Na'] = 1
C_int['Ca'] = 10e-4
C_ext['Ca'] = 1.5
z['Ca'] = 2

print(nernst_equation(C_int['K'], C_ext['K'], z['K']))
print(nernst_equation(C_int['Na'], C_ext['Na'], z['Na']))
print(nernst_equation(C_int['Ca'], C_ext['Ca'], z['Ca']))









