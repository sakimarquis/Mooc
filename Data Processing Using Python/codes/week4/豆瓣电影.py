# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:49:04 2018

@author: Saki
"""

import requests
r = requests.get('https://api.douban.com/v2/movie/subject/1291546')
data = r.json()
print(data["title"],data["rating"]['average'])