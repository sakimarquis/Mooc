# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:41:02 2018

@author: Saki
"""

import pandas as pd
import scipy
from scipy import io
features_struct = scipy.io.loadmat('E:\Study\Mooc\Machine Learning\Exercise\ex4\ex4data1.mat')
x = features_struct['X']
y = features_struct['y']
x1,x2 = x[0::2],x[1::2]
y1,y2 = y[0::2],y[1::2]

data_new = 'E:\Study\Mooc\Machine Learning\Exercise\ex4\data_new.mat'
scipy.io.savemat(data_new, {'x1':x1,'x2':x2,'y1':y1,'y2':y2})