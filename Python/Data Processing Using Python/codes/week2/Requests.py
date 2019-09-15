# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:04:17 2018

@author: Saki
"""
import requests

r = requests.get('https://book.douban.com/subject/30194861/comments/')
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()



'''为了反爬，有些网站会对Headers的User-Agent进行检测，需将headers信息
传递给get函数的headers参数，例如知乎，直接访问会返回500，
加上headers参数后可正确返回'''

re = requests.get('https://www.zhihu.com')

# headers可从http测试网站http://httpbin.org上获得
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
re = requests.get('https://www.zhihu.com', headers = headers)
re.status_code