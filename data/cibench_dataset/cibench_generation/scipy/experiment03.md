---
jupyter:
  title: Linear Algebra Operations with NumPy and SciPy
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 3
  num_steps: 7
  step_types:
    - num
    - text
    - text
    - num
    - num
    - num
    - num
  modules: 
    - numpy & scipy
    - scipy
    - scipy
    - scipy
    - scipy
    - scipy
    - scipy
---

Create a 2x2 matrix, A, where the first row is [1, 2] and the second row is [3, 4]. Calculate the determinant of the created matrix, A.
```python
import numpy as np
from scipy import linalg

A = np.array([[1, 2],[3, 4]])
det_A = linalg.det(A)
det_A
```

Calculate the inverse of the matrix, A. Display it.
```python
inv_A = linalg.inv(A)
inv_A
```

Find the eigenvalues and eigenvectors of the matrix, A. Display them.
```python
eigvals, eigvecs = linalg.eig(A)
print(eigvals)
print(eigvecs)
```

Using the matrix A, solve the system of linear equations represented by Ax = b where b is [5, 6]. Display the sum of x and keep it to two decimal places.
```python
b = np.array([5, 6])
x = linalg.solve(A, b)
round(x.sum(), 2)
```

Use SVD operation to decomposes the matrix, A, into 3 other matrices. Display the sum of s and keep it to two decimal places.
```python
U, s, Vh = linalg.svd(A)
round(s.sum(), 2)
```

Use LU decomposition factors the matric A. Display the sum of U and keep it to two decimal places.
```python
P, L, U = linalg.lu(A)
round(U.sum(), 2)
```

Use QR decomposition decomposes the matric A. Display the sum of R and keep it to two decimal places.
```python
Q, R = linalg.qr(A)
round(R.sum(), 2)
```