# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:20:19 2018

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

# test output type (different, p, better)
def test_q6():
    q6 = run_ttest()
    different, p, better = q6

    res = 'Type test: '
    res += ['Failed\n','Passed\n'][type(q6) == tuple]

    res += 'Test "different" type: '
    res += ['Failed\n','Passed\n'][type(different) == bool or type(different) == np.bool_]

    res += 'Test "p" type: '
    res += ['Failed\n','Passed\n'][type(p) == np.float64]

    res +='Test "better" type: '
    res += ['Failed\n','Passed\n'][type(better) == str]
    if type(better) != str:
        res +='"better" should be a string with value "university town" or  "non-university town"'
        return res
    res += 'Test "different" spelling: '
    res += ['Failed\n','Passed\n'][better in ["university town", "non-university town"]]
    return res
print(test_q6())