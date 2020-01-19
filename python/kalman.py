'''
Kalman filter example demo in Python
温度预测
室内温度恒定为23.5度。
根据经验预测时，温度是保持不变的，但是存在一个预测方差Q = 4e-4
但是测数时有一个测量误差，符合高斯分布，方差为R = 0.2^2
假定初始估计温度为25度
初始kalma系统方差为P = 1.0
'''
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.rcParams['figure.figsize'] = (10,8)

#inital parameters

n_iter = 100
sz = (n_iter,)
x = 23.5    #真实温度
z = np.random.normal(x,0.2,size=sz)  #测量值


#allocate apace for arrays
state_kalman = np.zeros(sz)  # 状态x的后验估计值
state_pre = np.zeros(sz)     # 状态x的先验预测值
P = np.zeros(sz)  
Pminus = np.zeros(sz)
K = np.zeros(sz)



R = 0.2**2                   # 温度测量时的方差
Q = 4e-4                     # 温度预测时的的方差

state_kalman[0] = 25         # 温度初始值
P[0] = 1.0                   # 温度初始估计方差


for	k in range(1,n_iter):
	#卡尔曼方程的五个公式
	state_pre[k] = state_kalman[k-1]    # 根据上一时刻卡尔曼估计值，直接预测本时刻
	Pminus[k] = P[k-1] + Q              # 存在预测误差

	
	K[k] = Pminus[k]/(Pminus[k] + R)    # kalman 增益	
	state_kalman[k] = state_pre[k] + K[k]*(z[k] - state_pre[k])	  # kalman 估计值
	P[k] = (1-K[k])*Pminus[k]
	

plt.figure()
plt.plot(z,'k+',label = '观测数据')
plt.plot(state_kalman,'b-',label = '后验估计')
plt.axhline(x,color = 'g',label = '真值')

plt.legend()
plt.title('Kalman Filter',fontweight = 'bold')
plt.xlabel('迭代次数')
plt.ylabel('温度幅值')



plt.figure()
valid_iter = range(1,n_iter)
plt.plot(valid_iter,Pminus[valid_iter],label = '先验误差')

plt.title('Kalman Filter',fontweight = 'bold')

plt.xlabel('迭代次数')
plt.ylabel('误差幅值')

plt.setp(plt.gca(),'ylim',[0,.05])
plt.show()
