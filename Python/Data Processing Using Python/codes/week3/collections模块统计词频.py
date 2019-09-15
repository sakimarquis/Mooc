# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:22:10 2018

@author: Saki
"""

import collections
import copy
s = "我 是 一个 测试 句子 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧 ， 重要 事情 说 三遍 ！"
s_list = s.split()
# 产生一份深拷贝避免remove()方法影响迭代
s_list_backup = copy.deepcopy(s_list)    
[s_list.remove(item) for item in s_list_backup if item in '，。！”“']
print(collections.Counter(s_list))