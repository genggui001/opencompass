---
jupyter:
  title: Solving Integrals and Differential Equations using Scipy in Python
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 5
  num_steps: 7
  step_types:
    - num
    - num
    - num
    - num
    - vis
    - vis
    - num
  modules: 
    - numpy & scipy
    - numpy & scipy
    - scipy
    - scipy
    - numpy & scipy & matplotlib
    - numpy & scipy & matplotlib
    - numpy & scipy
---

We will define a quadratic function `f(x) = x^2`. Compute the definite integral of the defined function from 0 to 1. Display the integral result and rounded to two decimal places.

```python
import numpy as np

def func(x):
    return x**2

from scipy import integrate

result, error = integrate.quad(func, 0, 1)
round(result, 2)
```

Compute the indefinite integral of the defined function, y'=y^2. Initial point is y0=0.5, x range from 0-1 with 100 intervals. Print the last value of the result with two decimal places.
```python
y0 = 0.5
x = np.linspace(0, 1, 100)

def func2(y, t):
    return y**2

y = integrate.odeint(func2, y0, x)
round(y[-1][0], 2)
```

Compute the double integral of a function `f(x, y) = x*y` over the rectangle `0 <= x <= 1`, `0 <= y <= 1`. Display the result and rounded to two decimal places.
```python
result, error = integrate.dblquad(lambda x, y: x*y, 0, 1, lambda x: 0, lambda x: 1)
round(result, 2)
```

Compute the triple integral of a function `f(x, y, z) = x*y*z` over the cube `0 <= x <= 1`, `0 <= y <= 1`, `0 <= z <= 1`. Display the result and rounded to two decimal places.
```python
result, error = integrate.tplquad(lambda x, y, z: x*y*z, 0, 1, lambda x: 0, lambda x: 1, lambda x, y: 0, lambda x, y: 1)
round(result, 2)
```

Solve the ordinary differential equation `dy/dx = -2y` with initial condition `y(0) = 1`. Plot the solution.
```python
import matplotlib.pyplot as plt

def func(y, x):
    return -2*y

y0 = 1
x = np.linspace(0, 5, 100)
y = integrate.odeint(func, y0, x)
plt.plot(x, y)
plt.show()
```

Solve the system of ordinary differential equations `du/dt = -2u` and `dv/dt = -2v` with initial conditions `u(0) = 1`, `v(0) = 0`. Plot the solution.
```python
def func(uv, t):
    u, v = uv
    return [-2*u, -2*v]

uv0 = [1, 0]
t = np.linspace(0, 5, 100)
uv = integrate.odeint(func, uv0, t)
u, v = uv.T
plt.plot(t, u)
plt.plot(t, v)
plt.show()
```

Solve the system of linear equations `2x + y = 1` and `x + y = 2`. Display the sum of result and rounded to two decimal places.
```python
from scipy import linalg

a = np.array([[2, 1], [1, 1]])
b = np.array([1, 2])
x = linalg.solve(a, b)
round(x.sum(), 2)
```
