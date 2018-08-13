# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:55:10 2018

@author: Saki
"""

def answer_seven():
    Top15 = answer_one()
    Top15['ratio'] = Top15['Self-citations'] / Top15['Citations']
    max_country = Top15.sort_values(by = 'ratio', ascending = False).iloc[0].name
    max_percentage = Top15['ratio'].max()
    max = (max_country,max_percentage)
    return max

answer_seven()