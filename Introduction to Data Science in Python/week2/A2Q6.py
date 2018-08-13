# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:37:47 2018

@author: Saki
"""

import pandas as pd
census_df = pd.read_csv('E:\Study\Mooc\Introduction to Data Science in Python\data\census.csv')

def answer_six():
    county = census_df[census_df['SUMLEV'] == 50]
    columns_to_keep = ['STNAME',
                       'CTYNAME',
                       'CENSUS2010POP']
    county = county[columns_to_keep]

    #得到州名
    states = set(county['STNAME'].values)

    top3popst = pd.DataFrame(data=None,columns=['STNAME', 'top3pop'],index=[0,1])
    count = 0
    for i in states:
        top3 = county[county['STNAME'] == i].sort_values(by = 'CENSUS2010POP', ascending = False).reset_index()
        top3pop = top3[0:3]['CENSUS2010POP'].sum()
        top3popst.loc[count] = [i,top3pop]
        count += 1
        top3popst = top3popst.sort_values(by = 'top3pop', ascending = False)

    return top3popst['STNAME'].values[0:3].tolist()

answer_six()