# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:04:36 2018

@author: Saki
"""

import pandas as pd

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    return recession_start[0]
def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''       
    return recession_end[0]

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''   
    return recession_bottom[0]

GDP = pd.read_excel("gdplev.xls",
                    usecols = [4,6])
GDP = GDP.iloc[214:285]#.reset_index()
GDP = GDP.reset_index().drop('index',axis = 1)
GDP.columns = ['period','chained_GDP']
chained_GDP = GDP['chained_GDP'].values

recession_start = []
recession_end = []
recession_bottom = []

flag = True
start = False
for i in range(4,len(GDP)):
    if not start and chained_GDP[i-1] < chained_GDP[i-2] and chained_GDP[i] < chained_GDP[i-1]:   
        if flag:
            recession_start.append(GDP['period'].values[i-1])
            start_index = i
            flag = False
            start = True
    if start and chained_GDP[i-1] > chained_GDP[i-2] and chained_GDP[i] > chained_GDP[i-1]:
        recession_end.append(GDP['period'].values[i])
        start = False
        end_index = i
        recession = GDP.iloc[range(start_index,end_index)]
        recession_bottom.append(recession.where(recession['chained_GDP'] == recession.chained_GDP.min()).dropna().period.values[0])
    else:
        flag = True