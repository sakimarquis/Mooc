# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:22:54 2018

@author: Saki
"""

import requests
kw  = {'q': 'Python dict'}
r = requests.get('http://cn.bing.com/search',params = kw)
r.url
print(r.text)