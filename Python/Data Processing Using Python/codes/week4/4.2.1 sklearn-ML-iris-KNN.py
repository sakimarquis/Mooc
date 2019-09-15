# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:06:22 2018

@author: Saki

分类学习算法KNN最近邻（k-nearest neighbor ，最简单的分类算法，新的观
测值的标签由n维空间中最靠近它的训练样本标签确定）判断萼片长度和宽度、花瓣
长度和宽度分别是5.0cm, 3.0cm, 5.0cm, 2.0cm的鸢尾花所属类别。

尝试用k-means聚类算法对原始数据进行聚类（3类）并观察聚类的正确率（注意，
类别用0，1，2表示，但并不限定表示某一类）。
"""

from sklearn import datasets

#获取iris数据集，可用dir(datasets)查看数据集
iris = datasets.load_iris()

# 利用KNN分类算法进行分类
from sklearn import neighbors , datasets
iris = datasets.load_iris()
knn = neighbors.KNeighborsClassifier()
# 从已有数据中学习
knn.fit(iris.data, iris.target)
# 利用分类模型进行未知数据的预测（确定标签）
knn.predict([[5.0, 3.0, 5.0, 2.0]])   

# 利用k-means聚类算法进行聚类
from sklearn import cluster, datasets
iris = datasets.load_iris()
kmeans = cluster.KMeans(n_clusters = 3).fit(iris.data)
pred = kmeans.predict(iris.data)   # 确定数据的类别
# 比较算法正确率
for label in pred:
    print(label, end = ' ')    # 打印预测出的各条数据的标签
print('\n')
for label in iris.target:
    print(label, end = ' ')    # 打印原始标注好的正确标签