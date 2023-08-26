from sklearn import metrics
import matplotlib.pylab as plt

plt.rc('font', family='Times New Roman')

y_true_1 = [1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
            0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

y_score_2 = [0.99, 0.98, 0.97, 0.93, 0.85, 0.80, 0.79, 0.75, 0.70, 0.65,
             0.64, 0.63, 0.55, 0.54, 0.51, 0.49, 0.30, 0.2, 0.1, 0.09]

precision1, recall1, _ = metrics.precision_recall_curve(y_true_1, y_score_2)
aupr1 = metrics.auc(recall1, precision1)  # the value of roc_auc1
print(aupr1)
plt.plot(recall1, precision1, 'b', label='AUC = %0.2f' % aupr1)
plt.show()


plt.rc('font', family='Times New Roman')

y_true_1 = [1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
            0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

y_score_2 = [0.99, 0.98, 0.97, 0.93, 0.85, 0.80, 0.79, 0.75, 0.70, 0.65,
             0.64, 0.63, 0.55, 0.54, 0.8, 0.49, 0.30, 0.2, 0.1, 0.09]

fpr1, tpr1, thresholds = metrics.roc_curve(y_true_1, y_score_2)
roc_auc1 = metrics.auc(fpr1, tpr1)  # the value of roc_auc1
print(roc_auc1)
plt.plot(fpr1, tpr1, 'b', label='AUC = %0.2f' % roc_auc1)
plt.show()
