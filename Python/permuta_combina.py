# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 19:34:57 2018

@author: Saki
"""

import itertools as iter

# product 笛卡尔积（有放回抽样排列）
base = 'ATCG'
result = iter.product(base, repeat=6)  # 因为内容太多, 所以返回生成器, 可以用list方法使其变成列表
print(len(set(result)))

# permutations 排列（不放回抽样排列）
print(list(iter.permutations('1234',4)))

# combinations 组合 (不放回抽样组合）
edges = range(10) 
print(list(iter.combinations(edges,2)))


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    
    #pools = [('A', 'B', 'C', 'D'), ('x', 'y')]
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    
    # 每有一个arg迭代一次
    for pool in pools:
        # 每次迭代把一个arg加到result里面
        # y是新添加的arg，x是在result里面的arg
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    # 迭代对象的indices
    indices = list(range(n))
    # 从迭代对象数量n取到n-r，r（需要排列的数量）个
    # cycles[i] = n - i
    cycles = list(range(n, n-r, -1))
    # 从迭代对象中，取r（需要排列的数量）个，
    # yield第一个对象
    yield tuple(pool[i] for i in indices[:r])
    while n:
        # 迭代r（需要排列的数量）次
        # i从r-1到0，对应cycles
        for i in reversed(range(r)):
            # cycles[i] = n - i
            cycles[i] -= 1
            # 如果cycles[i]被减到0了
            if cycles[i] == 0:
                # 如果i = 0，则把indices的第一位转移到最后一位
                indices[i:] = indices[i+1:] + indices[i:i+1]
                # cycles[i]变回初始值
                cycles[i] = n - i
            else:
                # 看不懂，猜测大概是改变indices来取不同pool的值
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        
        
        
import copy    #实现list的深复制
 
def combine(lst, l):
     result = []
     tmp = [0]*l
     length = len(lst)
     def next_num(li=0, ni=0):
        if ni == l:
            result.append(copy.copy(tmp))
            return
        for lj in range(li,length):
             tmp[ni] = lst[lj]
             next_num(lj+1, ni+1)
     next_num()
     return result


def permutation(lst,k):
     result = []
     length = len(lst)
     tmp = [0]*k
     def next_num(a,ni=0):
        if ni == k:
             result.append(copy.copy(tmp))
             return
         for lj in a:
             tmp[ni] = lj
             b = a[:]
             b.pop(a.index(lj))
             next_num(b,ni+1)
     c = lst[:]
     next_num(c,0)
     return result
 
# =============================================================================
# my implement
# =============================================================================
def combination_two(number_list):
    combination = []  
    for i in number_list:
        for j in number_list[i+1:]:
            edge.append(tuple([i,j]))
    return combination
            
            
            
    