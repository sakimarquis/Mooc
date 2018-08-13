d# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:53:06 2018

@author: Saki
"""
import pandas as pd

def get_list_of_university_towns():
    raw = pd.read_table(r"university_towns.txt",header = None)
    list = pd.DataFrame(columns = ['State','RegionName'])
    count = 0
    for i in range(len(raw)):
        if '[edit]' in raw.values[i][0]:
            State = raw.values[i][0].split('[')[0].rstrip()
        else:
            Region = raw.values[i][0].split('(')[0].rstrip()
            list.loc[count] = {'State': State, 'RegionName': Region}
            count += 1    
    return list

raw = pd.read_table(r"university_towns.txt",header = None)
list = pd.DataFrame(columns = ['State','RegionName'])
count = 0
for i in range(len(raw)):
    if '[edit]' in raw.values[i][0]:
        State = raw.values[i][0].split('[')[0].rstrip()
    else:
        Region = raw.values[i][0].split('(')[0].rstrip()
        list.loc[count] = {'State': State, 'RegionName': Region}
        count += 1
    