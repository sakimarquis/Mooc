# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:53:39 2018

@author: Saki
"""

def answer_thirteen():
    Top15 = answer_one()
    PopEst = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    PopEst = PopEst.apply(lambda x:format(x,','))
    return PopEst

answer_thirteen()