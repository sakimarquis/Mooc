# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:48:14 2018

@author: Saki

SVM最简单的是线性支持向量机，它尝试构建一个两个类别（不仅可用于二类分类，也可
以用于多类分类）的最大间隔超平面即能将两个类别分割开的直线，但如果数据是线性不
可分的，则要用到核函数，将数据映射到高维空间中寻找可区分数据的超平面。如果选择
合适的SVM参数、核函数和特征，则在模不大的数据集上其表现不错。
"""

from sklearn import datasets

#获取iris数据集，可用dir(datasets)查看数据集
iris = datasets.load_iris()

from sklearn import svm, datasets

iris = datasets.load_iris()
svc = svm.LinearSVC()
svc.fit(iris.data, iris.target) # 学习
svc.predict([[ 5.0, 3.0, 5.0, 2.0]])  # 预测