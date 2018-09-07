# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:56:06 2018

@author: Saki
"""

'''
用字典创建一个平台的用户信息（包含用户名和密码）管理系统，
新用户可以用与现有系统帐号不冲突的用户名创建帐号，已存在的
老用户则可以用用户名和密码登陆重返系统。建议基本框架为：
'''

useraccount= {}

def newusers():
    username = input("Username:")
    if username in useraccount:
        username = input("Username already used.\nUsername:")
    else:
        password = input("password:")
    useraccount[username] = password


def oldusers():
    username = input("Username:")
    password = input("password:")
    if useraccount[username] == password:  
        print(username, 'welcome back ')  
    else:  
        print('login incorrect') 
    … …

def login():
    option = '''
             (N)ew User Login 
             (O)ld User Login
             (E)xit
                    '''
    Enter the option
    … …

if __name__ == '__main__':  
    login() 
     