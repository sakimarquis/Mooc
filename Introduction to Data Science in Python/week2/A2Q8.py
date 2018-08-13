# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:34:59 2018

@author: Saki
"""

import pandas as pd
census_df = pd.read_csv('E:\Study\Mooc\Introduction to Data Science in Python\data\census.csv')

def answer_eight():
    county = census_df[census_df['SUMLEV'] == 50]

    columns_to_keep = ['STNAME',
                       'CTYNAME',
                       'REGION',
                       'POPESTIMATE2014',
                       'POPESTIMATE2015']

    county=county[columns_to_keep]

    county = county[(county['REGION']<=2) & (county['POPESTIMATE2015']>=county['POPESTIMATE2014'])]
    county = county.drop(['REGION','POPESTIMATE2014','POPESTIMATE2015'], axis = 1)
    query = county.copy()

    for i in range(len(county)):
        if county['CTYNAME'].values[i].split(' ')[0] != 'Washington':
            query = query.drop(county.index[i])
    return query

answer_eight()