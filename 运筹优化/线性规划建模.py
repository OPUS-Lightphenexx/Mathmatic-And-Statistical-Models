import pulp as pp

#先建立模型
Problem_Setting = pp.LpProblem(sense=pp.LpMaximize)

#添加变量,这里cat(变量类型)有三种
x = pp.LpVariable(name='x')
y = pp.LpVariable(name='y')
#其他类型
x2 = pp.LpVariable(name='x2',cat=pp.LpContinuous,upBound=None,lowBound=0)
x3 = pp.LpVariable(name='x3',cat=pp.LpBinary)
x4 = pp.LpVariable(name='x4',cat=pp.LpInteger)
#用字典设置多个相同类型的变量
x1 = {i:pp.LpVariable(name='x{}'.format(i),upBound=None,lowBound=0,cat=pp.LpContinuous) for i in range(10)}

#添加约束条件
Problem_Setting += (2 * x + 3 * y - 6 >= 0)
Problem_Setting += (x + y - 3 <= 0)
Problem_Setting += (y - 2 <= 0)

#建立目标函数
Problem_Setting += x + 3 * y

#进行求解
solve = Problem_Setting.solve()
print(solve)

#查看x和y的值
for vary in Problem_Setting.variables():
    print(vary,':',vary.value())

#选课策略线性规划建模


