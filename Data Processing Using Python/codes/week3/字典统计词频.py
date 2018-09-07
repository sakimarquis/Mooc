# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:23:52 2018

@author: Saki
"""

s_dict = {}
s = "我 是 一个 测试 句子 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧，重要 事情 说 三遍！"
s_list=s.split()
for item in s_list:
    if item.strip() not in "，。！“”":
        if item not in s_dict:
            s_dict[item] = 1
        else:
            s_dict[item] += 1
print(s_dict)