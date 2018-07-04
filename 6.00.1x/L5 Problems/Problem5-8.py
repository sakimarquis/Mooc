# -*- coding: utf-8 -*-
def isIn(char, aStr):
    if  len(aStr) == 0:
        return False
    if  len(aStr) == 1:
        return aStr == char
    if char == aStr[len(aStr)/2]:
        return True
    elif char > aStr[len(aStr)/2]:
        return isIn(char,aStr[len(aStr)/2:])  #下限不能等于0，不需要精确在中间划分
    else:
        return isIn(char, aStr[:len(aStr)/2])  #上限不能等于最后那位数

print isIn('r', 'bcddefmmppqrstxxxy')


def isInir(char, aStr):
    mid = aStr[len(aStr)/2 - 1:len(aStr)/2]
    while char != mid and len(aStr) > 1:
        mid = aStr[len(aStr) / 2 - 1:len(aStr) / 2]
        print aStr
        if char == mid:
            return True
        elif char > mid:
            aStr = aStr[len(aStr)/2-1:]
        else:
            aStr = aStr[:len(aStr)/2]
    return False

