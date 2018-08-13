# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:04:59 2018

@author: Saki
"""

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}

def answer_eleven():
    Top15 = answer_one().reset_index()
    Top15['Continent'] = Top15['Country'].copy()
    Top15['Continent'] = Top15.replace(ContinentDict)
    Top15['est_pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Continent = pd.DataFrame(index = ['Asia', 'Australia', 'Europe', 'North America', 'South America'], 
                             columns = ['size', 'sum', 'mean', 'std'])
    Continent['size'] = Top15.groupby('Continent').est_pop.count()
    Continent['sum']  = Top15.groupby('Continent').est_pop.sum()
    Continent['mean'] = Top15.groupby('Continent').est_pop.mean()
    Continent['std']  = Top15.groupby('Continent').est_pop.std()
    return Continent

answer_eleven()