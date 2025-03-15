---
jupyter:
  title: Experiment on Modifying Matplotlib Parameters and Styles
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 20
  num_steps: 6
  step_types:
    - num
    - vis
    - vis
    - num
    - vis  
    - vis
  modules: 
    - numpy & matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

We will generate an array of 100 values from 0 to 10, which will represent the x-coordinates for a sine wave. Corresponding y-coordinates are the sine of the x-coordinates.
Before we create the graph, display the default line width parameter of matplotlib.
```python
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
import matplotlib
matplotlib.rcParams['lines.linewidth']
```

Reset Matplotlib Parameters and set linewidth to 5 then plot the graph.
```python
import matplotlib.pyplot as plt
matplotlib.rcdefaults()
matplotlib.rcParams['lines.linewidth'] = 5
plt.plot(x, y)
plt.show()
```

We can also modify the matplotlib parameters within a temporary context. We will change the line width to 2 within a context and plot the graph.
```python
with plt.rc_context({'lines.linewidth': 2}):  # Temporary context modification
    plt.plot(x, y)  # Plot graph with temporary parameters
plt.show()
```

Display the current line width parameter of matplotlib.
```python
matplotlib.rcParams['lines.linewidth']
```

Change the figure size to 10,5 and dpi to 200 and plot the graph.
```python
matplotlib.rcParams['figure.figsize'] = [10, 5]  # Change figure size
matplotlib.rcParams['figure.dpi'] = 200  # Change dpi
plt.plot(x, y)
plt.show()
```

Reset Matplotlib parameters and use seaborn darkgrid style.
```python
matplotlib.rcdefaults()
plt.style.use('seaborn-darkgrid')  # Use a predefined style
plt.plot(x, y)  # Plot graph with style
plt.show()
```