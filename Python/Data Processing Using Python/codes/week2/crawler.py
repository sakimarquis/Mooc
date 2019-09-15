# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:53:04 2018

@author: Saki
"""

import requests
from bs4 import BeautifulSoup
import re
sum = 0

r = requests.get('https://book.douban.com/subject/30194861/?icn=index-editionrecommend')
soup = BeautifulSoup(r.text,"lxml")
#comments
pattern = soup.find_all('p', "comment-content")
for item in pattern:
    print(item.string+"\n")
#star
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)
for star in p:
    sum += int(star)
print(sum)