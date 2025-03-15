---
jupyter:
  title: Spatial Data Structures and Algorithms using Scipy
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 32
  num_steps: 4
  step_types:
    - vis
    - text
    - num
    - vis
  modules: 
    - numpy & scipy & matplotlib
    - scipy
    - scipy
    - numpy & scipy & matplotlib
---

Create a 3x3 grid of points. The grid will be defined in a numpy array where each point is represented as a list of its 'x' and 'y' coordinates. Then, Construct a Voronoi diagram from the points. Visualize the Voronoi diagram.

```python
import numpy as np
from scipy.spatial import Voronoi
from scipy.spatial import voronoi_plot_2d
import matplotlib.pyplot as plt

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
vor = Voronoi(points)

fig = voronoi_plot_2d(vor)
plt.show()
```

Print the ridge vertices and ridge points of the Voronoi diagram.

```python
print(vor.ridge_vertices)
print(vor.ridge_points)
```

Create a KDTree from the points array. Query the KDTree to find the three nearest neighbors of the point [1, 1]. Display the sum of the indices.

```python
from scipy.spatial import KDTree

kdtree = KDTree(points)

distances, indices = kdtree.query([1, 1], k=3)
sum(indices)
```

Create a rotation that rotates by 45 degrees around the z-axis. Apply the rotation to the points array. Plot the rotated points. 

```python
from scipy.spatial.transform import Rotation as R

r = R.from_euler('z', 45, degrees=True)
points_3d = np.hstack([points, np.zeros((points.shape[0], 1))])

rotated_points = r.apply(points_3d)
plt.scatter(rotated_points[:, 0], rotated_points[:, 1])
plt.show()
```