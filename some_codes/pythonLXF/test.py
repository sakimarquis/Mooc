# -*- coding: utf-8 -*-
import codecs
import string

def ReadSingleSelection(filename):
    """
    输入text文件中的测试题
    返回能导入进问卷网的text文件
    """
    SingleSelectionFile = codecs.open(filename, 'rb', 'gbk')
    all = [line.rstrip() for line in SingleSelectionFile.readlines()]
    choices = []
    SingleSelections = ""
    for line in all:
        if len(line) == 0:
            continue
        if line[0] == '#':
            choices = line.split('\t')
        SingleSelections += line+"[单选题]\n"
        for choice in choices[1:]:
            SingleSelections += choice + "\n"
        SingleSelections += "\n"
    return SingleSelections

print ReadSingleSelection("a.txt")
#line = "完全不符合	比较不符合	不确定	比较符合	非常符合"
