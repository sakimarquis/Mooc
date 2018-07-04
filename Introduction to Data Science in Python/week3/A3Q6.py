# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:45:38 2018

@author: Saki
"""

def answer_six():
    Top15 = answer_one()
    max_country = Top15.sort_values(by = '% Renewable', ascending = False).iloc[0].name
    max_percentage = Top15['% Renewable'].max()
    max = (max_country,max_percentage)
    return max

answer_six()