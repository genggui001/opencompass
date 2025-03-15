---
jupyter:
  title: Experiment - Matrix Operations using Numpy and Scipy in Python
  module: SciPy
  dataset: none
  difficulty: MIDDLE
  idx: 40
  num_steps: 6
  step_types:
    - num
    - num
    - num
    - num
    - num 
    - num
  modules: 
    - numpy & scipy
    - numpy & scipy
    - numpy & scipy
    - numpy & scipy
    - numpy & scipy
    - numpy & scipy
---

Create a two-dimensional array using numpy with elements [[1, 2, 5, 6], [3, 4, 7, 9], [3, -1, 5, 9], [-2, -4, 2, 7]]. Calculate the determinant of the array created and rounded with two decimals.
```python
import numpy as np
from scipy import linalg
arr = np.array([[1, 2, 5, 6], [3, 4, 7, 9], [3, -1, 5, 9], [-2, -4, 2, 7]])
det = linalg.det(arr)
round(det, 2)
```

Calculate the norm of the matrix and rounded with two decimals.
```python
norm = linalg.norm(arr)
round(norm, 2)
```

Create a new matrix with elements [[5, 1], [1, 6]] and compute the Cholesky decomposition of a matrix. Display the sum of the result and rounded with two decimals.
```python
c = np.array([[5, 1], [1, 6]])
c_cholesky = linalg.cholesky(c)
round(c_cholesky.sum(), 2)
```

Compute the QR decomposition of the first step array. Display the sum of the L and rounded with two decimals.
```python
P, L, U = linalg.lu(arr)
round(L.sum(), 2)
```

Compute the Schur decomposition of the first step array. Display the sum of the T and rounded with two decimals.
```python
T, Z = linalg.schur(arr)
round(T.sum(), 2)
```

Compute the Kronecker product of two arrays. Display the sum of the result and rounded with two decimals.
```python
kron_result = linalg.kron(arr, arr)
round(kron_result.sum(), 2)
```