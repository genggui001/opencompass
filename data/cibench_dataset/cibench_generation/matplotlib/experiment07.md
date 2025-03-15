---
jupyter:
  title: Creating and Customizing Grids in Python Using Matplotlib
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 7
  num_steps: 5
  step_types:
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
---

Generate an array of 100 numbers, evenly spaced between 0 and 10. This will serve as the x-coordinates of your plot. Then, generate the y-coordinates by taking the sine of the x-coordinates. This will create a sine wave. Add a Grid to the Plot.
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.grid(True)
plt.show()
```

Change the style of the grid lines to dashed and the color to red with width 0.5.
```python
plt.plot(x, y)
plt.grid(color='red', linestyle='--', linewidth=0.5)
plt.show()
```

Create two subplots. The first subplot has a sine wave with a red dashed grid, and the second subplot has a cosine wave with a blue dash-dot grid.
```python
plt.subplot(2,1,1)
plt.plot(x, y)
plt.grid(color='red', linestyle='--')
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))
plt.grid(color='blue', linestyle='-.')
plt.show()
```

Set the x-axis to have a grid line every 1 unit and the y-axis to have a grid line every 0.1 unit.
```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.grid(True)
plt.show()
```

Create a polar plot using the radius (`r`) and angle (`theta`) variables. Add grid lines to the plot.
```python
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
ax = plt.subplot(111, polar=True)
ax.plot(theta, r)
ax.grid(True)
plt.show()
```