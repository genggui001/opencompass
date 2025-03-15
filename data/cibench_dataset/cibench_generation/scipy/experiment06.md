---
jupyter:
  title: Interpolation Methods Comparison in Python
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 6
  num_steps: 5
  step_types:
    - vis
    - vis
    - vis
    - vis
    - num
  modules: 
    - numpy & scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - matplotlib
    - numpy
---

Define x = [0, 1, 2, 3, 4, 5], y = [0, 0.8, 0.9, 0.1, -0.8, -1]. Uses linear interpolation to get all the y_new values for x_new np.arange(0, 5, 0.1). Plot a scatter image of the interpolated values.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])

x_new = np.arange(0, 5, 0.1)
f = interpolate.interp1d(x, y)
y_new = f(x_new)
plt.scatter(x_new, y_new)
plt.show()
```

Uses cubic interpolation to get all the y_new values for x_new np.arange(0, 5, 0.1). Plot a scatter image of the interpolated values.

```python
f_cubic = interpolate.interp1d(x, y, kind='cubic')
y_new_cubic = f_cubic(x_new)
plt.scatter(x_new, y_new_cubic)
plt.show()
```

Change to splrep interpolation and plot a new scatter like previous step.

```python
tck = interpolate.splrep(x, y)
y_new_spline = interpolate.splev(x_new, tck)
plt.scatter(x_new, y_new_spline)
plt.show()
```

Plot all data sets - original, linear interpolated, cubic interpolated, and spline interpolated - together for comparison. Use different line styles and add labels for clarity.

```python
plt.plot(x, y, 'o', label='original data')
plt.plot(x_new, y_new, '-', label='linear interpolation')
plt.plot(x_new, y_new_cubic, '--', label='cubic interpolation')
plt.plot(x_new, y_new_spline, ':', label='spline interpolation')
plt.legend()
plt.show()
```

Evaluate the accuracy of different interpolation methods by comparing with the true function (sine in this case). Calculate the mean absolute error for each method. Only display the sum of all mean error and keep it to two decimals.

```python
y_true = np.sin(x_new)
error_linear = np.mean(np.abs(y_new - y_true))
error_cubic = np.mean(np.abs(y_new_cubic - y_true))
error_spline = np.mean(np.abs(y_new_spline - y_true))
round(error_linear+error_cubic+error_spline, 2)
```