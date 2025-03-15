---
jupyter:
  title: Experiment with Plot Aspect Ratios and Data Limits in Matplotlib
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 31
  num_steps: 4
  step_types:
    - vis
    - vis
    - vis
    - vis
  modules: 
    - matplotlib & numpy
    - matplotlib
    - matplotlib
    - matplotlib
---

Generate Data Points range from 0 - 2pi with 400 intervals. y = sin(x^2) and Plot the Data.
```python
import numpy as np
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
```

Set the Aspect Ratio to 'Equal' and Adjust the Data Limits x(0 - 2pi), y(-1.5 - 1.5).
```python
plt.plot(x, y)
plt.gca().set_aspect('equal', 'box')
plt.gca().set_xlim([0, 2 * np.pi])
plt.gca().set_ylim([-1.5, 1.5])
plt.show()
```

Set the Aspect Ratio to 2 and Adjust the Data Limits x(0 - 3pi), y(-2 - 2).
```python
plt.plot(x, y)
plt.gca().set_aspect(2)
plt.gca().set_xlim([0, 3 * np.pi])
plt.gca().set_ylim([-2, 2])
plt.show()
```

Modify the Aspect Ratio to 5 and Adjust the Data Limits x(0 - 4pi), y(-3 - 3).
```python
plt.plot(x, y)
plt.gca().set_aspect(5)
plt.gca().set_xlim([0, 4 * np.pi])
plt.gca().set_ylim([-3, 3])
plt.show()
```
