---
jupyter:
  title: Plotting a sine wave with customization using Python's matplotlib library
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 3
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
    - numpy & matplotlib
---

Generate a numpy array of 50 evenly spaced points between 0 and 4π. This will serve as the x-values for our plot. Compute the sine of each x-value to create the corresponding y-values.With read line color.
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4 * np.pi, 50)
y = np.sin(x)
plt.plot(x, y, color='red')
plt.show()
```

Customize the line style in the plot. Change the line style to dashed. Add circle markers. Change the marker color to blue.
```python
plt.plot(x, y, color='red', linestyle='dashed', marker='o', markerfacecolor='blue')
plt.show()
```

Increase the marker size to 10 and add a grid to the plot.
```python
plt.grid(True)
plt.plot(x, y, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
plt.show()
```

Based on setting above. Add a title, x-label, and y-label. Increase the line width to 2.
```python
plt.grid(True)
plt.plot(x, y, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10, linewidth=2)
plt.title('Sine Wave')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.show()
```

Based on setting above. Add a legend. Add a label to the line of 'sin(x)'.Change the figure size to 10x6 inches.
```python
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.plot(x, y, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10, linewidth=2, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
```
