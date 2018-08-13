# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 23:58:44 2018

@author: Saki
"""

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#全部是一个意思
for person in people:
    print(split_title_and_name(person)
for person in people:
    print(lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
list(map(split_title_and_name, people)) 
list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))