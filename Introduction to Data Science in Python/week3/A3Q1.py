# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:42:32 2018

@author: Saki
"""

import numpy as np
import pandas as pd

def answer_one():
    Energy = pd.read_excel("Energy Indicators.xls",
                           sheet_name = 'Energy',
                           usecols = [2,3,4,5])
    Energy = Energy.iloc[16:243]
    Energy.columns = ['Country','Energy Supply', 'Energy Supply per Capita', '% Renewable']
    Energy = Energy.replace({"...":np.nan})
    Energy['Country'] = Energy['Country'].str.split('[0123456789]').str[0].str.split(' \(').str[0]
    Energy = Energy.replace({"Republic of Korea":"South Korea",
                             "United States of America": "United States",
                             "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                             "China, Hong Kong Special Administrative Region": "Hong Kong"})
    Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000
    
    GDP = pd.read_csv("world_bank.csv")
    GDP_columns = GDP.iloc[3].copy()
    GDP_columns[:4] = GDP.iloc[3][:4]
    GDP_columns[4:] = GDP.iloc[3][4:].astype('int64')
    GDP.columns = GDP_columns.astype('str')
    GDP = GDP.iloc[4:268].replace({"Korea, Rep.": "South Korea", 
                   "Iran, Islamic Rep.": "Iran",
                   "Hong Kong SAR, China": "Hong Kong"})

    ScimEn = pd.read_excel("scimagojr-3.xlsx",column = 0)
     
    answer = pd.merge(ScimEn.iloc[0:15], Energy, on = 'Country')
    GDP_merge = GDP[['Country Name','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].rename(columns={'Country Name':'Country'})
    answer = pd.merge(answer, GDP_merge, on = 'Country').set_index('Country')
    return answer

answer_one()