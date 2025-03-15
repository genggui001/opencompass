---
jupyter:
  title: Visualizing Data with Scatter Plots and Matplotlib.
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 37
  num_steps: 6
  step_types:
    - vis
    - vis
    - exec
    - exec
    - exec
    - exec
  modules: 
    - numpy & matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

We will create two arrays, each of size 50, which will serve as the data for our x and y axes in the scatter plot and create a basic scatter plot of our data.
```python
import numpy as np
np.random.seed(10) 
x = np.random.rand(50)
y = np.random.rand(50)
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()
```

Remove the top and right borders of the plot. Change the color of the remaining plot borders to grey.
```python
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('blue')
ax.spines['bottom'].set_color('blue')
ax.scatter(x, y)
plt.show()
```

Increase the width of the plot borders to 1 and set the position of the plot borders to the center.
```python
fig, ax = plt.subplots()
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.scatter(x, y)
plt.show()
```

We can add a shadow to the scatter plot for a 3D effect.
```python
fig, ax = plt.subplots()
scatter = ax.scatter(x, y)
import matplotlib.patheffects
scatter.set_path_effects([
    matplotlib.patheffects.Stroke(linewidth=5, foreground='black'),
    matplotlib.patheffects.Normal()])
plt.show()
```

Change the background color of the plot to light grey.
```python
fig, ax = plt.subplots(facecolor='lightgrey')
ax.scatter(x, y)
plt.show()
```

Change the style of the markers in the scatter plot to square markers.
```python
fig, ax = plt.subplots(facecolor='lightgrey')
scatter = ax.scatter(x, y, marker='s')
plt.show()
```