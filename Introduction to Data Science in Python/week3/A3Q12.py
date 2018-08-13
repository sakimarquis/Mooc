# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:40:45 2018

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

def answer_twelve():
    Top15 = answer_one().reset_index()
    Top15['Continent'] = Top15['Country'].copy()
    Top15['Continent'] = Top15.replace(ContinentDict)
    Top15['bins for % Renewable'] = pd.cut(Top15['% Renewable'],5)
    return Top15.groupby(['Continent', 'bins for % Renewable']).Country.count()

answer_twelve()

