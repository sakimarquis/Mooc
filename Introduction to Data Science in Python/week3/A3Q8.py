# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:02:40 2018

@author: Saki
"""

def answer_eight():
    Top15 = answer_one()
    Top15['est_pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    third_country = Top15.sort_values(by = 'est_pop', ascending = False).iloc[2].name
    return third_country

answer_eight()