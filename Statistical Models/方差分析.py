import numpy
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import numpy as np

data = pd.read_csv(r'C:\Users\14380\Desktop\Mathmatic-Models\order_train1.csv')

data_numpy_test = pd.DataFrame([[1, 1, 32],
                     [1, 2, 35],
                     [1, 3, 35.5],
                     [1, 4, 38.5],
                     [2, 1, 33],
                     [2, 2, 36.5],
                     [2, 3, 38],
                     [2, 4, 39.5],
                     [3, 1, 36],
                     [3, 2, 37.5],
                     [3, 3, 39.5],
                     [3, 4, 43.5]],
                    columns=['A', 'B', 'value'])

model = ols('ord_qty~C(first_cate_code)',data=data).fit()
result = anova_lm(model)
print(result)

model2 = ols('value~C(A)+C(B)',data=data_numpy_test).fit()
result2 = anova_lm(model2)
print(result2)

model3 = ols('value~C(A)*C(B)',data=data_numpy_test).fit()
result3 = anova_lm(model3)
print(result3)

data_numpy_test.to_numpy()

df_t = pd.DataFrame(data_numpy_test.values.T)
print(len(df_t))
test = np.array(df_t)
print(test)
test_labels = np.array([2]*len(df_t))
print(test_labels)
