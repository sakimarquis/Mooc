# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 00:31:30 2018

@author: Saki

计算MovieLens 100k数据集中男性女性用户评分的标准差并输出。
数据集下载http://files.grouplens.org/datasets/movielens/ml-100k.zip
其中u.data 表示100k条评分记录，每一列的数值含义是：
user id | item id | rating | timestamp
u.user表示用户的信息，每一列的数值含义是：
user id | age | gender | occupation | zip code
u.item文件表示电影的相关信息，每一列的数值含义是：
movie id | movie title | release date | video release date |IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |

可能会用到的相关函数：
pandas.read_table(filepath_or_buffer, sep='\t', names=None)
pandas.pivot_table(data, values=None, columns=None, aggfunc='mean')
pandas.merge(left, right, how='inner')

先分别计算每个人电影评分的平均分再按性别求标准差
"""

import pandas as pd

#读取
ratings = pd.read_table('u.data', sep='\t',names=["user id","movie id","rating","timestamp"])
users = pd.read_table('u.user', sep='|',names=["user id","age","gender","occupation","zip code"])
movies = pd.read_table('u.item', sep='|',encoding='ISO-8859-1',names=["movie id","movie title","release date", "video release date", "IMDb URL", "unknown", "Action", "Adventure", "Animation", "Children’s", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"])
#movies = pd.DataFrame(moviesall, columns = ["movie id", "movie title"])

#合并
data = pd.merge(ratings, users, on = 'user id')
data = pd.merge(data, movies, on = 'movie id')
data = pd.DataFrame(data, columns = ["user id","movie id","rating","gender","movie title"])

#每个人电影评分的平均分
m = data.groupby('user id').rating.mean()

#新建一个dataframe放需要的数据
userstmp = users.sort_values(by = 'user id')
userstmp = pd.DataFrame(userstmp, columns = ["user id","gender"])
userstmp.index = range(1,len(userstmp) + 1) 
userstmp["meanrating"] = m

#求平均
std = userstmp.groupby('gender').meanrating.std()
print(std)