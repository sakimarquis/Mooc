# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 22:15:08 2018

@author: Saki

将Intel和IBM公司近一年来每个月开票价的平均值绘制在一张图中
"""

import requests
import re
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import time


def retrieve_quotes_historical(stock_code):
    quotes = []
    #抓取的股票url
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    #从抓取的网页中获取需要的信息，能打开则解码json，清理数据
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return [item for item in quotes if not 'type' in item]

def create_aveg_open(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = [] #时间序列
    #把时间转化成可读的格式
    for i in range(len(quotes)):
        x = date.fromtimestamp(quotes[i]['date'])
        y = date.strftime(x,'%Y-%m-%d')   
        list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes, index = list1) #添加时间index
    listtemp = []
    #生成月份列
    for i in range(len(quotesdf_ori)):
        temp = time.strptime(quotesdf_ori.index[i],"%Y-%m-%d")
        listtemp.append(temp.tm_mon)
    tempdf = quotesdf_ori.copy()
    tempdf['month'] = listtemp
    meanopen = tempdf.groupby('month').open.mean()
    return meanopen

open1 = create_aveg_open('INTC')
open2 = create_aveg_open('IBM')
plt.subplot(211)          
plt.plot(open1.index,open1.values,color='r',marker='o')
plt.subplot(212)
plt.plot(open1.index,open2.values,color='green',marker='o')

