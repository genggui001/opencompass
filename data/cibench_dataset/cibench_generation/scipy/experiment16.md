---
jupyter:
  title: Optimization Problems and Solutions Using scipy.optimize in Python
  module: SciPy
  dataset: None
  difficulty: NORMAL
  idx: 16
  num_steps: 4
  step_types:
    - num
    - num
    - num
    - num
  modules: 
    - scipy
    - numpy & scipy
    - numpy & scipy
    - numpy & scipy
---

Define a simple linear programming problem. We will use the objective function c = [-1, -2] and constraints A = [[1, 1], [-1, 1]], b = [1, 1]. Solve the linear programming problem using scipy.optimize's linprog function. Print the optimal value rounded with 2 decimals.

```python
from scipy.optimize import linprog

c = [-1, -2]
A = [[1, 1], [-1, 1]]
b = [1, 1]
x0_bounds = (0, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

round(res.fun, 2)
```

Define a non-linear programming problem. Here, our objective function is fun = lambda x: x[0]*x[1] - x[0] - x[1] and the constraint is cons = ({'type': 'ineq', 'fun': lambda x:  x[0]*x[1] - 1}). Solve the non-linear programming problem. Print the optimal value rounded with 2 decimals.

```python
from scipy.optimize import minimize
import numpy as np
fun = lambda x: x[0]*x[1] - x[0] - x[1]
cons = ({'type': 'ineq', 'fun': lambda x:  x[0]*x[1] - 1})
x0 = np.array([1.0, 1.0])
res = minimize(fun, x0, constraints=cons)

round(res.fun, 2)
```

Define a multi-dimensional optimization problem. The objective function is fun = lambda x: x[0]**2 + x[1]**2 + x[2]**2 and the constraint is cons = ({'type': 'eq', 'fun': lambda x:  x[0] + x[1] + x[2] - 1}). Solve the multi-dimensional optimization problem. Print the optimal value rounded with 2 decimals.

```python
fun = lambda x: x[0]**2 + x[1]**2 + x[2]**2
cons = ({'type': 'eq', 'fun': lambda x:  x[0] + x[1] + x[2] - 1})
x0 = np.array([0.0, 0.0, 0.0])
res = minimize(fun, x0, constraints=cons)

round(res.fun, 2)
```

Define an optimization problem with bounds. The objective function is fun = lambda x: x[0]**2 + x[1]**2 and the constraint is cons = ({'type': 'ineq', 'fun': lambda x:  x[0] + x[1] - 1}). Solve the optimization problem with bounds using scipy.optimize's minimize function. Print the optimal value and solution.

```python
fun = lambda x: x[0]**2 + x[1]**2
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] + x[1] - 1})
x0 = np.array([0.0, 0.0])
bounds = [(0, None), (0, None)]

res = minimize(fun, x0, constraints=cons, bounds=bounds)

round(res.fun, 2)
```
