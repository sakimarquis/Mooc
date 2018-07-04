# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:42:21 2018

@author: Saki
"""

def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()

answer_five()