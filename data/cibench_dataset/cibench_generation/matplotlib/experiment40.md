---
jupyter:
  title: Demonstrate the process of generating and plotting various types of grids.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 40
  num_steps: 6
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy & matplotlib
    - numpy & matplotlib
    - numpy & matplotlib
    - numpy & matplotlib
    - numpy & matplotlib
    - matplotlib
---

Generate a grid with 5 points in the x-axis and 5 points in the y-axis, both ranging from 0 to 1. Plot the simple grid with the points represented as blue dots and lines.
```python
import numpy as np
x, y = np.mgrid[0:1:5j, 0:1:5j]
import matplotlib.pyplot as plt
plt.triplot(x.flatten(), y.flatten(), 'bo-')
plt.show()
```

Generate a grid with 20 points in the x-axis and 20 points in the y-axis, both ranging from 0 to 2. This grid is denser than the previous one.Plot the simple grid with the points will be represented as red dots and lines.
```python
x, y = np.mgrid[0:2:20j, 0:2:20j]
plt.triplot(x.flatten(), y.flatten(), 'ro-')
plt.show()
```

Generate a mesh using random coordinates and triangles.Plot the triangular mesh with the points represented as green dots and lines.
```python
triangles = np.array([[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5]])
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])
import matplotlib.tri as mtri
triang = mtri.Triangulation(x, y, triangles)
plt.triplot(triang, 'go-')
plt.show()
```

Generate a grid with 50 random points in the x-axis and 50 random points in the y-axis, both ranging from 0 to 1.Plot the random grid with the points represented as black dots and lines.
```python
x, y = np.random.rand(2, 50)
plt.triplot(x, y, 'ko-')
plt.show()
```

Generate z-values from the x and y coordinates using a mathematical function, specifically the sine and cosine functions. Afterwards, create a filled contour plot.
```python
z = np.sin(2 * np.pi * x) * np.cos(2 * np.pi * y)
plt.tricontourf(x, y, z)
plt.show()
```

Create a 3D surface plot using the x, y, and z values generated in the previous steps.
```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x, y, z)
plt.show()
```