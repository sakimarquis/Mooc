# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:53:36 2018

@author: Saki
"""

import pandas as pd
scores = pd.read_excel('scores.xlsx')
scores.boxplot()