# -*- coding: utf-8 -*-

import string

def ReadQ(filename):
    """
    输入text文件中的测试题
    返回能导入进问卷网的text文件
    """
    QFile = open(filename, "r")
    all = [line.rstrip() for line in QFile.readlines()]
    choices = []
    Qs = ""
    type = '单选题'
    for line in all:
        if len(line) == 0:
            continue
        if line[0] == '$':
            type = line.strip()
        if line[0] == '#':
            choices = line.split('\t')
        uline = line.decode('gbk')
        utype = type.decode('utf-8')
        Qs += uline +'['+ utype + ']\n'
        for choice in choices[1:]:
            uchoice = choice.decode('gbk')
            Qs += uchoice + "\n"
        Qs += "\n"
    return Qs

def ReWriteText(filename,data):
    Qs = ReadQ("a.txt")
    
    pass
    #f = open(filename, 'w')
    #f.write(data)

print ReadQ("a.txt")
#ReWriteText("b.txt",ReadQ("a.txt"))
#line = "完全不符合	比较不符合	不确定	比较符合	非常符合"
