# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 09:58:04 2020

@author: saki
"""

import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('01.png')
plt.imshow(image)
plt.show()

rgb = []
k = 20
for i in range(3):
    U, sigma, VT = np.linalg.svd(image[:,:,i]) # full_matrices=False
    U = U[:,:k]
    sigma = (sigma * np.eye(1080))[:k,:k]
    VT = VT[:k,:]
    rgb.append(U @ sigma @ VT)

compressed = np.dstack(rgb)
plt.imshow(compressed)
plt.show()
    
