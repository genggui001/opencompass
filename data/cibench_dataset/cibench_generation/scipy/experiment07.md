---
jupyter:
  title: Spatial Data Structures and Algorithms Experiment
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 7
  num_steps: 7
  step_types:
    - vis
    - num
    - num
    - vis
    - vis
    - num
    - num
  modules: 
    - numpy & matplotlib
    - scipy
    - scipy
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy
    - numpy
---

Visualize the following points of [[0.93, 0.97],[0.82, 0.36],[0.8 , 0.92],[0.79, 0.33],[0.31, 0.41],[0.09, 0.79],[0.6 , 0.85],[0.95, 0.67],[0.81, 0.75],[0.01, 0.83]] using a scatter plot. Use the first column of the points as the x-coordinates and the second column as the y-coordinates.
```python
import numpy as np
import matplotlib.pyplot as plt

points = np.array([[0.93, 0.97],[0.82, 0.36],[0.8 , 0.92],[0.79, 0.33],[0.31, 0.41],[0.09, 0.79],[0.6 , 0.85],[0.95, 0.67],[0.81, 0.75],[0.01, 0.83]])

plt.scatter(points[:,0], points[:,1])
plt.show()
```

Construct a KDTree from these points. Query the KDTree for the nearest neighbor of the point (0.5, 0.5) using the query method. Only display its distance and rounded to two decimal places.
```python
from scipy.spatial import KDTree

tree = KDTree(points)
dist, idx = tree.query([0.5, 0.5])
round(dist, 2)
```

Similarly, query the KDTree for the nearest neighbors of the points (0.5, 0.5) and (0.2, 0.2). Only display the sum of these nesrest distances and rounded to two decimal places.
```python
dists, idxs = tree.query([[0.5, 0.5], [0.2, 0.2]])
round(dists.sum(), 2)
```

Compute the Convex Hull of these points. Then, plot the Convex Hull along with the points. Draw lines connecting the points forming the convex hull.
```python
from scipy.spatial import ConvexHull

hull = ConvexHull(points)
plt.scatter(points[:,0], points[:,1])
for simplex in hull.simplices:
   plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.show()
```

Compute the Voronoi diagram of the points. Visualize the Voronoi diagram along with the points.
```python
from scipy.spatial import Voronoi, voronoi_plot_2d

vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.scatter(points[:,0], points[:,1])
plt.show()
```

Compute a square distance matrix containing the distances, taken pairwise, between the points. Only display the max distance and rounded to two decimal places.
```python
from scipy.spatial import distance_matrix

dist_matrix = distance_matrix(points, points)
round(dist_matrix.max(), 2)
```

Using the distance matrix, find and print the pair of points with the shortest distance. Only display the shortest distance and rounded to two decimal places.
```python
np.fill_diagonal(dist_matrix, np.inf)
min_dist = np.min(dist_matrix)
round(min_dist, 2)
```