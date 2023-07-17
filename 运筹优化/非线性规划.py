import numpy as np
from scipy.optimize import minimize


def objective():
    v = lambda x: (2 + x[0]) / (1 + x[1]) - 3 * x[0] + 4 * x[2]
    return v


def con():
    cons = ({'type': 'ineq', 'fun': lambda x: x[0] - 0.1},
            {'type': 'ineq', 'fun': lambda x: -x[0] + 0.9},
            {'type': 'ineq', 'fun': lambda x: x[1] - 0.1},
            {'type': 'ineq', 'fun': lambda x: -x[1] + 0.9},
            {'type': 'ineq', 'fun': lambda x: x[2] - 0.1},
            {'type': 'ineq', 'fun': lambda x: -x[2] + 0.9})
    return cons


cons = con()

# 设置初始猜测值
x0 = np.asarray((0.5, 0.5, 0.5))

optimize = minimize(objective(), x0, method='SLSQP', constraints=cons)
print(optimize.fun)
print(optimize.success)
print(optimize.x)