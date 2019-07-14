# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:28:26 2019

@author: saki
""" 
import os  

file_path = '文件路径' # 文件路径
file_extension = '.文件扩展名' # 文件扩展名

def get_current_filename(file_path, file_extension = None):
    if file_extension:
        l = []
        for file in os.listdir(file_path):
            if os.path.splitext(file)[-1] == file_extension:
                l.append(file)
        print(l)
    else:
        print(os.listdir(file_path))
        

def get_filename(file_path, file_extension = None):
    for root, dirs, files in os.walk(file_path):
        if file_extension:
            l = []
            for file in files:  
                if os.path.splitext(file)[-1] == file_extension:  
                    l.append(os.path.join(root, file))
                    print(root,file)
        else:
            print(root,files)