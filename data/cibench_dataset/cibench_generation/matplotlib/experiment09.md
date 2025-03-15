---
jupyter:
  title: Visualizing Data with Contour Plots 
  module: matplotlib
  dataset: none
  difficulty: DIFFICULT
  idx: 9
  num_steps: 5
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy & matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - numpy & matplotlib
---

We define an array of 100 points between -10 and 10 for both x and y. Then, create a grid of points using numpy's meshgrid function. Calculate the corresponding values for a 2D Gaussian distribution and create a basic contour plot of the Gaussian distribution data using matplotlib's contour function.
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 20)
plt.contour(X, Y, Z)
plt.show()
```

Increase the number of contour levels to 20 to provide a more detailed view of the distribution.Fill the areas between the contour levels.
```python
plt.contourf(X, Y, Z, 20)
plt.show()
```

Add a colorbar to the plot that indicates the values of the contour levels. Change the color map of the plot to 'viridis' to provide a different view of the distribution.
```python
contour = plt.contourf(X, Y, Z, 20, cmap='viridis')
plt.colorbar(contour)
plt.show()
```

Add labels to the contour lines using matplotlib's clabel function and change the color to black.
```python
contour = plt.contour(X, Y, Z, 20, colors='black')
plt.clabel(contour, inline=True, fontsize=8)
plt.show()
```

Define a function that depends on x and y of `np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)`, and generate a contour plot for this function.
```python
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, 20, cmap='RdGy')
plt.show()
```
