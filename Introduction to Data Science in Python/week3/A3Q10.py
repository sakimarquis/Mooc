# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:21:44 2018

@author: Saki
"""

def answer_ten():
    Top15 = answer_one()
    median = Top15['% Renewable'].median()
    Top15['HighRenew'] = Top15['% Renewable'].copy()
    Top15['HighRenew'] = Top15['HighRenew'].where(Top15['% Renewable'] >= median,0).where(Top15['% Renewable'] < median,1)
    Top15.sort_index(inplace=True)
    return Top15['HighRenew'].astype('int64')

answer_ten()