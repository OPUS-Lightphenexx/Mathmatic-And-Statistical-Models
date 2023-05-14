import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 1, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

plt.subplot(221)
plt.imshow(harvest,cmap="YlGn")
plt.colorbar()
for i in range(7):
    for j in range(7):
        text = plt.text(j, i, harvest[i, j],ha='center',va="center", color="black")
plt.subplot(222)
plt.imshow(harvest,cmap='PuOr')
plt.colorbar()
for i in range(7):
    for j in range(7):
        text = plt.text(j, i, harvest[i, j],ha='center',va="center", color="black")
plt.subplot(223)
plt.imshow(harvest)
for i in range(7):
    for j in range(7):
        text = plt.text(j, i, harvest[i, j],ha='center',va="center", color="black")
plt.colorbar()
plt.subplot(224)
plt.imshow(harvest,cmap='Wistia')
plt.colorbar()
for i in range(7):
    for j in range(7):
        text = plt.text(j, i, harvest[i, j],ha='center',va="center", color="black")
plt.show()

