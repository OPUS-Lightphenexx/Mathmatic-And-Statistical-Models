import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


#创建3d图形
ax3 = plt.axes(projection='3d')

# 曲线参数方程绘制
#t = np.linspace(0,100,100)
#x1 = -t**2
#y1 = 2*t**0.5
#z1 = t

#三维函数
x = np.arange(-5,5,0.5)
y = np.arange(-5,5,0.5)
X , Y = np.meshgrid(x,y)
z = (X**2-Y)**0.5

#绘制三维三点图
#data = np.random.randint(0,300,size=(40,40))
#x3, y3 ,z3 =data[0],data[1],data[2]

#print(data)


# 绘制图形
#plt.plot(x1, y1, z1, label='Test Function')#参数方程
ax3.plot_surface(X,Y,z,label='Test Function')
#ax3.scatter(x3,y3,z3)

# 显示图形
plt.show()
