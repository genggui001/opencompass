---
jupyter:
  title: Generate several heatmaps using different colormaps and customizations in Matplotlib.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 35
  num_steps: 7
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy & matplotlib
    - matplotlib
    - numpy & matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

Generate a 10x10 array of random values for the heatmap. Set the colormap to 'hot' and interpolation to 'nearest'. You can also add a colorbar.
```python
import numpy as np
data = np.random.rand(10, 10)
import matplotlib.pyplot as plt
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()
```

Change the colormap of the heatmap to 'cool'. Then change the interpolation method of the heatmap to 'bicubic'.
```python
plt.imshow(data, cmap='cool', interpolation='bicubic')
plt.colorbar()
plt.show()
```

Create a linear gradient going from left to right using a colormap. For this, use the 'viridis' colormap. 
```python
gradient = np.linspace(0, 1, 256)  # Create linear gradient
gradient = np.vstack((gradient, gradient))  # Stack for imshow
plt.imshow(gradient, aspect='auto', cmap=plt.get_cmap('viridis'))
plt.show()
```


Create 4 subplots each with a different colormap based on the first step data. Use 'hot', 'cool', 'spring', and 'winter' colormaps.
```python
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
colormaps = ['hot', 'cool', 'spring', 'winter']
for ax, cmap in zip(axs.flat, colormaps):
    im = ax.imshow(data, cmap=cmap)
    fig.colorbar(im, ax=ax)
plt.show()
```

Create a custom colormap that goes from blue to red. 
```python
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('custom', ['blue', 'red'], N=256)
plt.imshow(data, cmap=cmap)
plt.colorbar()
plt.show()
```

Make a colormap discrete. Make a discrete colormap with 5 colors. 
```python
from matplotlib.colors import BoundaryNorm
cmap = plt.get_cmap('hot')
norm = BoundaryNorm(range(6), cmap.N)
plt.imshow(data, cmap=cmap, norm=norm)
plt.colorbar()
plt.show()
```

Create an alpha colormap, where the colors have different alpha values.
```python
from matplotlib.colors import ListedColormap
cmap = plt.get_cmap('hot')
alphas = np.linspace(0, 1, cmap.N)
cmap_alpha = ListedColormap(cmap(np.arange(cmap.N)) * alphas[:, np.newaxis])
plt.imshow(data, cmap=cmap_alpha)
plt.colorbar()
plt.show()
```