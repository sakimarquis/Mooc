# -*- coding: utf-8 -*-
"""
Retrieve dji stock data

@author: Dazhuang
"""

'''
在“http://money.cnn.com/data/dow30/”上抓取道指
成分股数据并将30家公司的代码、公司名称和最近一次
成交价放到一个列表中输出。
'''

import requests
import re

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">
                                (.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)
                                <\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
print(dji_list)