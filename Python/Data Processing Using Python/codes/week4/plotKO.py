# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:00:14 2018

@author: Saki
"""

# -*- coding: utf-8 -*-
"""
plot the average close of KO

@author: Dazhuang
"""

import requests
import re
import json
import pandas as pd
from datetime import date
import time
import matplotlib.pyplot as plt

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('KO')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
quotesdf = quotesdf_ori.drop(['date'], axis = 1)
listtemp = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],"%Y-%m-%d")
    listtemp.append(temp.tm_mon)
tempdf = quotesdf.copy()
tempdf['month'] = listtemp
closeMeansKO = tempdf.groupby('month').close.mean()
x = closeMeansKO.index
y = closeMeansKO.values
plt.plot(x, y)
plt.savefig('1.jpg')