import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\14380\Desktop\Mathmatic-Models\order_train1.csv')

cov_matrix = data.cov()

sns.heatmap(cov_matrix,annot=True,cmap='coolwarm')
plt.title('cov')
plt.show()