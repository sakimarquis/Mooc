# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:37:11 2018

@author: Saki
"""
import pandas as pd
import numpy as np
from scipy import stats

def run_ttest():
    house = convert_housing_data_to_quarters().reset_index()
    university = get_list_of_university_towns()
    university['is_university'] = 1
    house['PriceRatio'] = house['2008q2']/(house['2009q2'])
    
    university = pd.merge(house,university, on=['State','RegionName'], how='left')
    university['is_university'] = university['is_university'].fillna(0)
    unitown = university[university['is_university'] == 1]['PriceRatio']
    non_unitown = university[university['is_university'] == 0]['PriceRatio']
    
    t = stats.ttest_ind(unitown, non_unitown, nan_policy = 'omit')
    pvalue = t[1]
    
    if pvalue < 0.01:
        different = True
    else:
        different = False
        
    if unitown.mean() < non_unitown.mean():
        better = "university town"
    else:
        better = "non-university town"
    answer = (different,pvalue,better)
    return answer

# 517*2(region State) get_list_of_university_towns()
# recession_start[0]  '2008q3'
# recession_end[0]  '2009q4'
# recession_bottom[0]  '2009q2'
# housing_data 10730 rows x 67 columns(time) convert_housing_data_to_quarters()

house = convert_housing_data_to_quarters().reset_index()
university = get_list_of_university_towns()
university['is_university'] = 1
house['PriceRatio'] = house['2008q2']/(house['2009q2'])

university = pd.merge(house,university, on=['State','RegionName'], how='left')
university['is_university'] = university['is_university'].fillna(0)
unitown = university[university['is_university'] == 1]['PriceRatio']
non_unitown = university[university['is_university'] == 0]['PriceRatio']

t = stats.ttest_ind(unitown, non_unitown, nan_policy = 'omit')
pvalue = t[1]

if pvalue < 0.01:
    different = True
else:
    different = False
    
if unitown.mean() < non_unitown.mean():
    better = "university town"
else:
    better = "non-university town"



    

