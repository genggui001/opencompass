---
jupyter:
  title: Exploring Numerical Optimization and Curve Fitting with Python Libraries
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 2
  num_steps: 3
  step_types:
    - num
    - num
    - num
  modules: 
    - numpy & scipy
    - numpy & scipy
    - scipy
---

Define a quadratic function with a sine component. The function is defined as f(x) = x^2 + 10sin(x). Use BFGS method to find the minimum of the function. Display the result and keep to two decimal places.

```python
import numpy as np
from scipy import optimize

def func(x):
    return x**2 + 10*np.sin(x)

result = optimize.minimize(func, x0=0)
print(round(result.x[0], 2))
```

Define a new function as f(x) = x^2 + 8sin(x). Use the Nelder-Mead optimization method to find the minimum. Display the result and keep to two decimal places.

```python
def func2(x):
    return x**2 + 8*np.sin(x)
result = optimize.minimize(func2, x0=0, method='Nelder-Mead')
print(round(result.x[0], 2))
```

Find the root of the first function. Display the result and keep to two decimal places.
```python
root = optimize.root(func, x0=1)
print(round(root.x[0], 2))
```
