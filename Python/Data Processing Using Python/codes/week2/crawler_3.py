# -*- coding: utf-8 -*-
"""
Crawler
@author: Dazhuang
"""

'''
请爬取网页（http://italy2014.fivb.org/en/competit
ion/results_and_statistics）上的数据

提示：由于包含信息的源代码分在3行，所以在处理时要
使用多行模式（用flags=re.M表示），并且要把换行时
的空白字符表示出来（用\s+可表示多个空白字符）
'''
import requests
import re
r = requests.get('http://italy2014.fivb.org/en/competition/results_and_st
                 atistics')
r.encoding = r.apparent_encoding
pattern = re.compile('<td><a id="wcbody_0_wcgridpade50e7ca82ec64ee2b9
                     1ea4cc6c4e00c6_1_PlayerStatisticsTable_BestScorer
                     s_Name_.*?" href="/en/competition\/teams\/.*?\/p
                     layers/.*?id=.*?">(.*?)</a></td>\s+<td id="wcbody
                     _0_wcgridpade50e7ca82ec64ee2b91ea4cc6c4e00c6_1_P
                     layerStatisticsTable_BestScorers_TeamCell_.*?"><a
                     id="wcbody_0_wcgridpade50e7ca82ec64ee2b91ea4cc6c4
                     e00c6_1_PlayerStatisticsTable_BestScorers_Team_.*
                     ?" href="/en/competition/teams/.*?">(.*?)</a></td>
                     \s+<td>(.*?)</td>\s+<td>(.*?)</td>\s+<td>(.*?)</td
                     >\s+<td>(.*?)</td>',flags=re.M)
p = re.findall(pattern, r.text)
print(p)

