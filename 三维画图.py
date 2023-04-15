import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


#创建3d图形
ax3 = plt.axes(projection='3d')

# 曲线参数方程绘制
t = np.linspace(0,100,100)
x1 = -t**2
y1 = 2*t**0.5
z1 = t
plt.plot(x1, y1, z1, label='Test Function')#参数方程
#plt.show()
#三维函数
x = np.arange(-5,5,0.5)
y = np.arange(-5,5,0.5)
X , Y = np.meshgrid(x,y)
z = X**2-Y
ax3.plot_surface(X,Y,z,label='Test Function')
#plt.show()
#绘制三维三点图
data = np.random.randint(0,300,size=(40,40))
x3, y3 ,z3 =data[0],data[1],data[2]
ax3.scatter(x3,y3,z3)
#plt.show()
#print(data)


#网格化图形
plt.show()

fig_test = plt.figure()
ax = fig_test.add_subplot(projection='3d')

x2 = np.arange(-5,5,0.5)
y4 = np.arange(-5,5,0.5)
X4,Y4 = np.meshgrid(x2,y4)
Z3 = -X**2+Y**3

ax.plot_wireframe(X4, Y4, Z3, rstride=1, cstride=1)

plt.show()

