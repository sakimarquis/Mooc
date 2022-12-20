import numpy as np
import matplotlib.pyplot as plt
wheat_and_bread = np.array([[0.5,5],[0.6,5.5],[0.8,6],[1.1,6.8],[1.4,7]])
sample_x=wheat_and_bread[:,0]
sample_y=wheat_and_bread[:,1]
#单次更新权重，对个数据集计算一个平均梯度
def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, points.shape[0]):
        #计算单个样本的梯度
        x = points[i][0]
        y = points[i][1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    #更新参数
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]
#回归直线函数值，用于画回归线
def compute_value(b,m,point):
    return m*point+b
range_x=np.arange(0,2,0.05)
#更新权重
def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    #打开动态显示
    plt.ion()
    for i in range(num_iterations):
        #单次迭代更新权重
        b, m = step_gradient(b, m, points, learning_rate)
        #清除图像
        plt.cla()
        plt.title('iter %d'%i)
        #散点图
        plt.scatter(sample_x,sample_y)
        #回归曲线
        plt.plot(range_x,compute_value(b,m,range_x))
        plt.pause(0.01)
    plt.ioff()
    plt.show()
    
    #return [b, m]
gradient_descent_runner(wheat_and_bread, 1, 1, 0.01, 100)

