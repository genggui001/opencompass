---
jupyter:
  title: Create a streamplot visualization of a vector field.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 33
  num_steps: 6
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy
    - matplotlib & numpy
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

Generate a grid of points in the x-y plane. The range is set from -5 to 5 in both dimensions, 100 points should be generated in each dimension.Create a simple vector field. U = -1 - X^2 + Y and V = 1 + X - Y^2. speed = sqrt(X^2 + Y^2).
```python
import numpy as np
Y, X = np.mgrid[-5:5:100j, -5:5:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```

Create a streamplot of the vector field. The color of the streamlines is set according to the speed of the vectors. The color map is set to 'autumn'.
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=speed, cmap='autumn')
fig.colorbar(strm.lines)
plt.show()
```

Modify the color map of the streamplot to 'winter' and visualize the plot.
```python
fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=speed, cmap='winter')
fig.colorbar(strm.lines)
plt.show()
```

Set color map to winter and change the density of the streamlines to 0.6.
```python
fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=speed, cmap='winter', density=0.6)
fig.colorbar(strm.lines)
plt.show()
```

Set color map to winter and change the density of the streamlines to 0.6, linewidth to 1.
```python
fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=speed, linewidth=1, cmap='winter', density=0.6)
fig.colorbar(strm.lines)
plt.show()
```

Modify the color of the streamlines to be based on the U. Add arrows to the streamlines. Set the size of the arrows to 2. Then, visualize the streamplot.
```python
fig, ax = plt.subplots()
strm = ax.streamplot(X, Y, U, V, color=U, linewidth=1, cmap='winter', density=0.6, arrowsize=2)
fig.colorbar(strm.lines)
plt.show()
```