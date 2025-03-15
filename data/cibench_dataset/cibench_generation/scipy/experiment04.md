---
jupyter:
  title: Analysis and Visualization of a 3x3 Matrix
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 4
  num_steps: 4
  step_types:
    - num
    - num
    - num
    - vis
  modules: 
    - numpy & scipy
    - scipy
    - scipy
    - matplotlib
---

Define a 3x3 matrix A with elements ranging from 1 to 9. Compute and print the norm of the matrix A. Display it and keep to two decimal places.
```python
import numpy as np
from scipy import linalg
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
norm_A = linalg.norm(A)
round(norm_A, 2)
```

Vector b is defined as [0, 1, 2]. Compute and print the dot product of vectors b and A. Display the sum of result and keep to two decimal places.
```python
b = np.array([0,1,2])
dot_bx = np.dot(b, A)
round(dot_bx.sum(), 2)
```

Compute and print the cross product of vectors b and A.  Display the sum of result and keep to two decimal places.
```python
cross_bx = np.cross(b, A)
round(cross_bx.sum(), 2)
```

Visualize the matrix A using a heatmap and add a colorbar to the plot.
```python
import matplotlib.pyplot as plt

plt.imshow(A, cmap='viridis')
plt.colorbar(label='Value')
plt.title('Matrix A')
plt.show()
```
