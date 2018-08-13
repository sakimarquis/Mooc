# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:08:31 2018

@author: Saki
"""
import numpy as np
import pandas as pd

def answer_three():
    Top15 = answer_one()
    avgGDP = Top15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].apply(lambda x:x.mean(),axis = 1)
    return avgGDP.sort_values(ascending = False)

answer_three()