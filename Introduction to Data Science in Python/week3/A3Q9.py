# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:07:15 2018

@author: Saki
"""

def answer_nine():
    Top15 = answer_one()
    Top15['est_pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citations per person'] = Top15['Citable documents'] / Top15['est_pop']
    corr = Top15['Energy Supply per Capita'].corr(Top15['Citations per person'])
    return corr

answer_nine()