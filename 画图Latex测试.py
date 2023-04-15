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


