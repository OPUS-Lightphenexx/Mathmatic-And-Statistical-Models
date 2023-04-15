import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)
y = x**2+x**3

plt.plot(x,y)
plt.grid()
plt.title('Matplotlib Latex Text On Graph')
plt.xlabel(r'$\frac{x^2}{2}$')

text_test = r'$\frac{\sin{\frac{x^2}{2}}}{\cos{x}}$'
plt.text(-0.25,1.6,text_test,fontsize=40)

plt.show()

def Write_Latex_Matplotlib(x:str,y,z:str):
    plt.text(0,0.9,x,fontsize = y)
    plt.grid()
    plt.title('Matplotlib Latex Text On Graph')
    plt.xlabel(z)
    plt.show()


print(Write_Latex_Matplotlib(r'$\frac{1}{2}$ The Test Function',20))


