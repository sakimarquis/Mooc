# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 10:40:26 2018

@author: Saki
"""

adict = {'carl':4,
          'alan':2,
          'bob':1,
          'danny':3}

def sort_by_value(adict):
    items=adict.items()    
    backitems = [[v[1],v[0]] for v in items]  
    backitems.sort()
    return [backitems[i][1] for i in range(0,len(backitems))]

 
sorted(adict.items(), key = lambda d: d[1])
sorted(adict, key = lambda d: d[1], reverse = True)

sorted(adict, key = lambda x: (adict[x], x))
sorted(adict, key = lambda x: (-adict[x], x))
sorted(adict, key = lambda x: adict[x])
