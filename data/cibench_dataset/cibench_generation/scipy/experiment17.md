---
jupyter:
  title: Performing Sparse and Dense Matrix Operations in Python
  module: SciPy
  dataset: None
  difficulty: NORMAL
  idx: 17
  num_steps: 6
  step_types:
    - text
    - text
    - text
    - text
    - text
    - text
  modules: 
    - numpy & scipy
    - scipy
    - scipy
    - numpy
    - scipy
    - numpy & scipy
---

Generate a sparse matrix of size 5x5 with some non-zero elements. The non-zero elements are 1, 2, 3, 4 and 5 at diagonal of the matrix respectively. Print the generated matrix to check its content.
```python
import numpy as np
from scipy import sparse
data = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 1, 2, 3, 4])
indptr = np.array([0, 1, 2, 3, 4, 5])

matrix_with_data = sparse.csr_matrix((data, indices, indptr), shape=(5, 5))
print(matrix_with_data)
```

Convert the sparse matrix to a dense matrix. Print the dense matrix.
```python
dense_matrix = matrix_with_data.toarray()
print(dense_matrix)
```

Convert the dense matrix back to a sparse matrix. Print the sparse matrix.
```python
sparse_matrix = sparse.csr_matrix(dense_matrix)

print(sparse_matrix)
```

Define a vector 'b' with elements from 1 to 5. Solve the linear system Ax=b with the dense matrix A and vector b using numpy's linear algebra solver. Print the solution 'x' obtained from solving the linear system with the dense matrix.
```python
b = np.array([1,2,3,4,5])
x = np.linalg.solve(dense_matrix, b)
print(x)
```

Solve the linear system Ax=b with the sparse matrix A and the vector b using scipy's sparse linear algebra solver. Print the solution 'x_sparse' obtained from solving the linear system with the sparse matrix.
```python
from scipy.sparse import linalg

x_sparse = linalg.spsolve(sparse_matrix, b)
print(x_sparse)
```

Compare the cost time of the dense and sparse matrix calculations above. And print the method that is faster. 'dense' or 'sparse'.
```python
import time

start_time = time.time()
x = np.linalg.solve(dense_matrix, b)
end_time = time.time()
dense_time = end_time - start_time

start_time = time.time()
x_sparse = linalg.spsolve(sparse_matrix, b)
end_time = time.time()
sparse_time = end_time - start_time

print('sparse')
```
