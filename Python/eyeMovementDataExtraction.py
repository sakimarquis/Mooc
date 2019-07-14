# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:56:25 2018

@author: saki
"""

SUBJECTS_NUM = 1 #有几个被试,从1开始到n，中间不能断
BLOCKS_NUM = 7 #有几个Block,从1开始到n，中间不能断

import pandas as pd

def first(data):
    if int(data[0]) <= 3 and int(data[-1]) == 5:
        return 1
    else:
        return 0

def get_values(data,df):
    select_idx = []
    for k,v in data.items():
        if abs(v) > 1:
            if v < 0:
                select_idx.append(k)
            else:
                select_idx.append(k+1)
    ans = []            
    for i in select_idx:
        select = df[df['general order'] == i]
        x = str(list(select['triger or event'])[0])[0] + ", " + str(float(select['onset of saccade']))
        ans.append(x)
    return ans

results = []

for subject in range(1,SUBJECTS_NUM+1):
    for block in range(1,BLOCKS_NUM+1):
        data = pd.DataFrame(pd.read_excel(str(subject)+'yd'+str(block)+'_microsac.xls'))
        data['str_tri'] = data['triger or event'].astype(str) 
        data['cond1'] = data['str_tri'].apply(first)
        filter1 = data[(data['cond1'] == 1) & (data['onset of saccade'] >= 800)]
        max_diff = filter1.groupby(['triger or event'])['saccade amplitude'].diff(periods=1)
        ans = get_values(max_diff,data)
        results += ans
        
df = pd.concat([pd.DataFrame([i], columns=['A']) for i in results])
df.to_csv('result.csv')
