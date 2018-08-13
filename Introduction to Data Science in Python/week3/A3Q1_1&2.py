# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:38:50 2018

@author: Saki
"""
import numpy as np
import pandas as pd

Energy = pd.read_excel("E:\Study\Mooc\Introduction to Data Science in Python\data\Energy Indicators.xls",
                       sheet_name = 'Energy',
                       usecols = [2,3,4,5])
#去头尾，重命名列
Energy = Energy.iloc[16:243]
Energy.columns = ['Country','Energy Supply', 'Energy Supply per Capita', '% Renewable']
#替换...
Energy = Energy.replace({"...":np.nan})
#替换数字和括号内的东西（括号前的空格）
Energy['Country'] = Energy['Country'].str.split('[0123456789]').str[0].str.split(' \(').str[0]
Energy = Energy.replace({"Republic of Korea":"South Korea",
                         "United States of America": "United States",
                         "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                         "China, Hong Kong Special Administrative Region": "Hong Kong"})
Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000

GDP = pd.read_csv("E:\Study\Mooc\Introduction to Data Science in Python\data\world_bank.csv")

#因为年份的数据类型是float64，所以直接把他作为列名的话，年份变成如
#2018.0这样的数据，所以先要转换成int64去掉小数后面的，再转换成str
GDP_columns = GDP.iloc[3].copy()
GDP_columns[:4] = GDP.iloc[3][:4]
GDP_columns[4:] = GDP.iloc[3][4:].astype('int64')
GDP.columns = GDP_columns.astype('str')
GDP = GDP.iloc[4:268].replace({"Korea, Rep.": "South Korea", 
               "Iran, Islamic Rep.": "Iran",
               "Hong Kong SAR, China": "Hong Kong"})

ScimEn = pd.read_excel("E:\Study\Mooc\Introduction to Data Science in Python\data\scimagojr-3.xlsx",column = 0)
 
answer = pd.merge(ScimEn.iloc[0:15], Energy, on = 'Country')

GDP_merge = GDP[['Country Name','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].rename(columns={'Country Name':'Country'})

answer = pd.merge(answer, GDP_merge, on = 'Country').set_index('Country')