---
jupyter:
  title: Make a 3D surface plot of sin(sqrt(x^2 + y^2)) with customizations using Matplotlib's mplot3d.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 39
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - numpy & matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

Create a base figure for 3D plotting. Generate two 1-D arrays for X and Y coordinates ranging from -5 to 5 with 100 points. Create a grid of points from the X and Y coordinates.
```python
import numpy as np
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
```

Define a function that calculates the Z coordinates Z which returns the sine of the square root of the sum of the squares of X and Y. Plot the 3D surface using X, Y, and Z. Label the X, Y, and Z axes. Set a title for the plot.Display the plot.
```python
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))
Z = f(X, Y)
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')
plt.show()
```

Change the color map of the surface plot to 'hot'.Set the limit for the Z axis between -1.01 and 1.01.Add a color bar to the plot. Set shrink to 0.5 and aspect to 5.
```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(-1.01, 1.01)
surf = ax.plot_surface(X, Y, Z, cmap='hot')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
```

Rotate the plot to get a better view. Set elev to 30 and azim to 120.
```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.view_init(elev=30, azim=120)
plt.show()
```
