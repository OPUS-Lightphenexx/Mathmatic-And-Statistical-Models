import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


#Bernouli大数定理
Samples1 = np.zeros(100)
for i in range(1,100):
    test1 = np.random.randint(0,2,100)
    sum1 = sum(test1)
    Samples1[i]=sum1/i

#plt.plot(Samples1)


#蒙特卡洛算法

#计算pi的近似值
m=1000
n=0
Samples2 = np.zeros(m)
for i in range(m):
    x = np.random.random()
    y = np.random.random()
    if math.sqrt(x**2+y**2)<1:
        n +=1
pi = 4*n/m
x = np.random.random(1000)
y = np.random.random(1000)
#if math.sqrt(x**)
#plt.scatter(x,y)
x1 = np.linspace(0,1,100)
y1 = np.sqrt(1-x1**2)
#plt.plot(x1,y1)

#计算积分
x3 = np.linspace(0,1,num=100)
y3 = np.log(1 + x3) / (1 + x3**2)
#plt.plot(x3,y3,'-',color='red')


m=100
n=0
for i in range(m):
    x6 = np.random.random()
    y6 = np.random.random()
    if np.log(1+x6)/(1+x6**2)>y6:
        n += 1

#plt.scatter(x,y)
result = n/m
print(result)


#以Bernouli大数定理进行展开画图
#计算pi值
n = 0
Bernouli_pi_zeros = np.zeros(5000)
for i in range(1,5000):
    dotsx = np.random.random()
    dotsy = np.random.random()
    if math.sqrt(dotsx**2+dotsy**2)<1:
        n +=1
    Bernouli_pi_zeros[i]=4*n/i

#plt.plot(Bernouli_pi_zeros)

#计算积分的值
f = 0
Bernouli_integral_zeros = np.zeros(1000)
for i in range(1,1000):
    x7 = np.random.random()
    y7 = np.random.random()
    if np.log(1 + x7) / (1 + x7 ** 2) > y7:
        f += 1
    Bernouli_integral_zeros[i]=f/i

plt.plot(Bernouli_integral_zeros)

plt.show()



