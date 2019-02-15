# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:03:39 2018

@author: Saki

将所有的点看成是一个簇
当簇小于数目k时
    对于每一个簇
        计算总误差
        在给定的簇上进行K-均值聚类,k值为2
        计算将该簇划分成两个簇后总误差
    选择是的误差最小的那个簇进行划分
"""

def biKmeans(dataSet, k, distMeas=distEclud):
    m = shape(dataSet)[0]
    # 这里第一列为类别，第二列为SSE
    clusterAssment = mat(zeros((m,2)))
    # 看成一个簇是的质心
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList =[centroid0] #create a list with one centroid
    for j in range(m):    #计算只有一个簇是的误差
        clusterAssment[j,1] = distMeas(mat(centroid0), dataSet[j,:])**2

    # 核心代码
    while (len(centList) < k):
        lowestSSE = inf
        # 对于每一个质心，尝试的进行划分
        for i in range(len(centList)):
            # 得到属于该质心的数据
            ptsInCurrCluster =\ dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]
            # 对该质心划分成两类
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            # 计算该簇划分后的SSE
            sseSplit = sum(splitClustAss[:,1])
            # 没有参与划分的簇的SSE
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
            print "sseSplit, and notSplit: ",sseSplit,sseNotSplit
            # 寻找最小的SSE进行划分
            # 即对哪一个簇进行划分后SSE最小
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
                
        # 这里是更改其所属的类别，其中bestClustAss = splitClustAss.copy()
        # 是进行k-means后所返回的矩阵，其中第一列为类别，第二列为SSE值，因为当k=2
        # 是k-means返回的是类别0，1两类，因此这里讲类别为1的更改为其质心的长度，而
        # 类别为0的返回的是该簇原先的类别。
        
        # 举个例子： 
        # 例如：目前划分成了0，1两个簇，而要求划分成3个簇，则在算法进行时，假设对1进
        # 行划分得到的SSE最小，则将1划分成了2个簇，其返回值为0，1两个簇，将返回为1
        # 的簇改成2，返回为0的簇改成1，因此现在就有0，1，2三个簇了。    
        bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList) #change 1 to 3,4, or whatever
        bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit
        print 'the bestCentToSplit is: ',bestCentToSplit
        print 'the len of bestClustAss is: ', len(bestClustAss)
        # 其中bestNewCents是k-means的返回簇中心的值，其有两个值，分别是第一个簇，
        # 和第二个簇的坐标(k=2)，这里将第一个坐标赋值给 centList[bestCentToSp
        # lit] = bestNewCents[0,:].tolist()[0],将另一个坐标添加到centList
        # 中 centList.append(bestNewCents[1,:].tolist()[0]) 
        centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]#replace a centroid with two best centroids 
        centList.append(bestNewCents[1,:].tolist()[0])
        clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:]= bestClustAss#reassign new clusters, and SSE
    return mat(centList), clusterAssment
