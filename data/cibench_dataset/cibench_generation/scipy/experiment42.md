---
jupyter:
  title: Creating a weighted graph and computing properties using numpy, scipy and matplotlib
  module: SciPy
  dataset: none
  difficulty: MIDDLE
  idx: 42
  num_steps: 6
  step_types:
    - exec
    - text
    - num
    - text
    - text
    - text
  modules: 
    - numpy
    - scipy
    - scipy
    - scipy
    - scipy
    - scipy
---


Define a 2D numpy array (7x7) filled with zeros, which will function as the adjacency matrix for the graph. Populate the adjacency matrix with edge weights. For instance, adjacency_matrix[0][1] = 2 means there is an edge between node 0 and node 1 with a weight of 2. Create a matrix of following weighted adjacency: [0][1] = 2,[0][2] = 1,[1][3] = 1,[1][4] = 3,[2][1] = 3,[2][5] = 4,[3][4] = 2,[4][5] = 1,[5][6] = 1.
```python
import numpy as np
adjacency_matrix = np.zeros((7, 7))
adjacency_matrix[0][1] = 2
adjacency_matrix[0][2] = 1
adjacency_matrix[1][3] = 1
adjacency_matrix[1][4] = 3
adjacency_matrix[2][1] = 3
adjacency_matrix[2][5] = 4
adjacency_matrix[3][4] = 2
adjacency_matrix[4][5] = 1
adjacency_matrix[5][6] = 1
```

Compute the depth first order of the graph with node 0 as the root. Print the depth first order.
```python
from scipy.sparse import csgraph
dfo = csgraph.depth_first_order(adjacency_matrix, 0)
print(dfo)
```

Compute the connected components of the graph. Display the number of connected components
```python
n_components, labels = csgraph.connected_components(adjacency_matrix)
n_components
```

Compute the Laplacian matrix of the graph. Print the Laplacian matrix.
```python
laplacian_matrix = csgraph.laplacian(adjacency_matrix)
print(laplacian_matrix)
```

Compute the shortest path between all pairs of nodes using the Floyd-Warshall algorithm. Print the shortest path matrix.
```python
floyd_warshall_path = csgraph.floyd_warshall(adjacency_matrix)
print(floyd_warshall_path)
```

Compute the breadth first order of the graph with node 0 as the root. Print the breadth first order.
```python
bfo = csgraph.breadth_first_order(adjacency_matrix, 0)
print(bfo)
```
