---
jupyter:
  title: Creating and Plotting Paths using Matplotlib and Numpy in Python.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 44
  num_steps: 6
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

We first create a list of (x, y) points and corresponding set of path codes. List of path points [(1.58, -2.57), (0.35, -1.1), (-1.75, 2.0), (0.375, 2.0), (0.85, 1.15), (1.58, -2.57)]. These are then used to create a Path instance.Plot the path. We first create a subplot and a Patch instance from the Path instance. Define the x and y limits of the plot to frame the path. Then display the plot.
```python
import matplotlib.path as mpath
import matplotlib.pyplot as plt
Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.LINETO, (0.35, -1.1)),
    (Path.LINETO, (-1.75, 2.0)),
    (Path.LINETO, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
fig, ax = plt.subplots()
import matplotlib.patches as mpatches
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
plt.show()
```

Label the points according to their path codes. Add text to the plot to indicate the points.
```python
fig, ax = plt.subplots()
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)
ax.text(1.58, -2.57, 'MOVETO')
ax.text(0.35, -1.1, 'LINETO')
ax.text(-1.75, 2.0, 'LINETO')
ax.text(0.375, 2.0, 'LINETO')
ax.text(0.85, 1.15, 'LINETO')
ax.text(1.58, -2.57, 'CLOSEPOLY')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
plt.show()
```

Create a more complex path. In this case, we will create a path that represents a sine wave.
```python
import numpy as np
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
vertices = np.column_stack([x, y])
path = mpath.Path(vertices)
fig, ax = plt.subplots()
patch = mpatches.PathPatch(path, facecolor='none', edgecolor='b')
ax.add_patch(patch)
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1.5, 1.5)
plt.show()
```

Create a closed path. These are similar to the previous paths, but with an additional command to close the path.
```python
vertices = np.array([(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 1.5), (0, 0)])
codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
path = mpath.Path(vertices, codes)
fig, ax = plt.subplots()
patch = mpatches.PathPatch(path, facecolor='none', edgecolor='b')
ax.add_patch(patch)
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 2)
plt.show()
```

Create a path with curves.
```python
vertices = np.array([(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 1.5), (0, 0)])
codes = [Path.MOVETO, Path.CURVE3, Path.CURVE4, Path.LINETO, Path.CURVE3, Path.CLOSEPOLY]
path = mpath.Path(vertices, codes)
fig, ax = plt.subplots()
patch = mpatches.PathPatch(path, facecolor='none', edgecolor='b')
ax.add_patch(patch)
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 2)
plt.show()
```

Combine multiple paths into a single path.Lastly, create a path from a polygon.
```python
path1 = mpath.Path([(0, 0), (1, 0), (1, 1), (0, 0)], [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY])
path2 = mpath.Path([(0, 0), (0, 1), (-1, 1), (0, 0)], [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY])
path = mpath.Path(np.concatenate([path1.vertices, path2.vertices]), np.concatenate([path1.codes, path2.codes]))
fig, ax = plt.subplots()
patch = mpatches.PathPatch(path, facecolor='none', edgecolor='b')
ax.add_patch(patch)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 1.5)
plt.show()
```