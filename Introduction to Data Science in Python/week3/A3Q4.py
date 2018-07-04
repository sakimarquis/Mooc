# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:31:31 2018

@author: Saki
"""

def answer_four():
    Top15 = answer_one()
    GDP_change = Top15.loc[answer_three().index[5]]['2015'] - Top15.loc[answer_three().index[5]]['2006']
    return GDP_change

answer_four()