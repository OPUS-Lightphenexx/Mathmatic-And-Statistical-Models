import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\14380\Desktop\Mathmatic-Models\order_train1.csv')

correlation_matrix1 = data.corr(method='pearson')
correlation_matrix2 = data.corr(method='spearman')
correlation_matrix3 = data.corr(method='Kendall')


sns.heatmap(correlation_matrix1, annot=True, cmap='coolwarm')
plt.title('Pearson')
plt.show()

sns.heatmap(correlation_matrix2,annot=True,cmap='coolwarm')
plt.title('Spearman')
plt.show()

sns.heatmap(correlation_matrix3,annot=True,cmap='coolwarm')
plt.title('Kendall')
plt.show()