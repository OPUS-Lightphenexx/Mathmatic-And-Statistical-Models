import numpy as np

def parabolic_approximation(f, a, b, n):
    # 使用抛物线法计算定积分近似值
    # f: 被积函数
    # a, b: 积分区间
    # n: 区间数
    h = (b - a) / n
    I = 0
    for i in range(n):
        xi = a + i * h
        xj = a + (i + 1) * h
        xm = (xi + xj) / 2
        A = [[xm ** 2, xm, 1], [xi ** 2, xi, 1], [xj ** 2, xj, 1]]
        b = [f(xm), f(xi), f(xj)]
        abc = np.linalg.solve(A, b)
        I += abc[0] * (xj**3 - xi**3) / 3 + abc[1] * (xj**2 - xi**2) / 2 + abc[2] * (xj - xi)
    return I

result1 = parabolic_approximation(lambda x:x**2+x**3,0,1,10)
print(result1)
#值:result1 = 0.5833333333333334

