# -*- coding: utf-8 -*-
"""
Get quotesdf

@author: Dazhuang
"""

import requests
import re
import json
import pandas as pd

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('AXP')
quotesdf = pd.DataFrame(quotes)
print(quotesdf)