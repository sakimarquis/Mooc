# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 23:53:02 2018

@author: Saki
"""

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split('. ')[1]

list(map(split_title_and_name,people))