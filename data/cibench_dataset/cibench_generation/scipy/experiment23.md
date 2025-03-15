---
jupyter:
  title: Calculating Different Types of Distances Between Data Points
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 23
  num_steps: 5
  step_types:
    - num
    - num
    - num
    - num
    - text
  modules: 
    - numpy & scipy
    - scipy
    - scipy
    - scipy
    - numpy & scipy
---

Start by generating two 3-dimensional points using NumPy arrays. Let's use points (1,2,3) and (4,5,6) for this example. Compute the Euclidean and Cityblock distance between the two points. Display the absolution difference between these two distances and rounded to two decimal places.
```python
import numpy as np

point1 = np.array((1, 2, 3))
point2 = np.array((4, 5, 6))
from scipy.spatial import distance

dist = distance.euclidean(point1, point2)
dist_cityblock = distance.cityblock(point1, point2)
round(abs(dist_cityblock - dist), 2)
```


Calculate the Minkowski distance between the two points with p=3. Compute the Cosine distance between the two points. Display the absolution difference between these two distances and rounded to two decimal places.
```python
dist_minkowski = distance.minkowski(point1, point2, p=3)
dist_cosine = distance.cosine(point1, point2)
round(abs(dist_minkowski - dist_cosine), 2)
```

Compute the Correlation distance between the two points. Compute the Chebyshev distance between the two points. Display the absolution difference between these two distances and rounded to two decimal places.
```python
dist_correlation = distance.correlation(point1, point2)
dist_chebyshev = distance.chebyshev(point1, point2)
round(abs(dist_correlation - dist_chebyshev), 2)
```

Generate two binary points. Let's use points [0,1,0,1,0] and [1,0,1,0,1] for this example. Compute the Hamming distance between the binary points and Jaccard distance. Display the absolution difference between these two distances and rounded to two decimal places.
```python
binary_point1 = [0, 1, 0, 1, 0]
binary_point2 = [1, 0, 1, 0, 1]

dist_hamming = distance.hamming(binary_point1, binary_point2)
dist_jaccard = distance.jaccard(binary_point1, binary_point2)

round(abs(dist_jaccard - dist_hamming), 2)
```

Create an array of 2-dimensional points using NumPy arrays. Let's use points [(1,2),(3,4),(5,6),(7,8),(9,10)] for this example. Compute the pairwise distances between all points. Convert the pairwise distances into a square matrix. Generate a distance matrix using the Cityblock distance.
```python
points = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
dist_matrix = distance.pdist(points)

dist_matrix_square = distance.squareform(dist_matrix)
dist_matrix_cityblock = distance.pdist(points, metric='cityblock')
dist_matrix_square_cityblock = distance.squareform(dist_matrix_cityblock)
print(dist_matrix_square_cityblock)
```
