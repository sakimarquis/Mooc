# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:35:20 2018

@author: Saki
"""
import numpy as np
import pandas as pd
census_df = pd.read_csv('E:\Study\Mooc\Introduction to Data Science in Python\data\census.csv')
def answer_seven():
    county = census_df[census_df['SUMLEV'] == 50]
    pop = county[['CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].reset_index().drop('index', axis = 1)
    max_diff = 0

    for i in range(len(pop)):
        tmp = pop.loc[i,['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
        diff = tmp.max() - tmp.min()
        if diff > max_diff:
            max_diff = diff
            max_index = i

    return pop.loc[max_index,'CTYNAME']

answer_seven()
