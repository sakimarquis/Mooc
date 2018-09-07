# -*- coding: utf-8 -*-

'''
1.定义函数countchar()按字母表顺序统计字符串中26个字母出现的
次数（不区分大小写）。例如字符串“Hope is a good thing.”的
统计结果为：

[1, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 3, 1, 0, 0, 1, 1,
 0, 0, 0, 0, 0, 0]’
'''

def countchar(l):
    count = [0] * 26
    for i in l.lower():
        if i.isalpha():
            count[ord(i)-ord('a')] += 1
    return count


list = "Hope is a good thing."
print (countchar(list))
