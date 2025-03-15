---
jupyter:
  title: Plotting a Vector Field using Python.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 46
  num_steps: 2
  step_types:
    - exec
    - vis
  modules: 
    - numpy
    - matplotlib
---

File Path: none.

Create a coordinate grid for the x and y axis. Let the range be from -5 to 5 (inclusive) with a step size of 1.
Define a vector field where the u component corresponds to the x coordinate and the v component is the negative of the y coordinate.
```python
import numpy as np
x,y = np.meshgrid(np.arange(-5,6,1), np.arange(-5,6,1))
u = x
v = -y
```

Set it to a 10x10 square for better visualization. Plot the vector field using the quiver function. Set the scale parameter to 20 to control the size of the arrows. Define the headlength, headaxislength and headwidth of the arrows to 4.5 for better visibility. Add labels to the x and y axis and also provide a title.
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.quiver(x, y, u, v, scale=20, headlength=4.5, headaxislength=4.5, headwidth=4.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Vector Field')
plt.show()
```
