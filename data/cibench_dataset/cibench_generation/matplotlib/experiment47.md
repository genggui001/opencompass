---
jupyter:
  title: Demonstrate how to plot two mathematical functions (sine and cosine) using the matplotlib library in Python.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 47
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
    - matplotlib
---

Generate a sequence of numbers from 0 to 10 using numpy linspace function. Compute the sine and cosine of these numbers using numpy functions sin() and cos().
Plot the sine and cosine values against the generated sequence on the same graph. Assign labels 'sin(x)' and 'cos(x)' to these plots. Add a Legend.
```python
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
import matplotlib.pyplot as plt
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.legend()
plt.show()
```

Reposition the legend to the upper left corner of the plot and display the plot.
```python
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.legend(loc='upper left')
plt.show()
```

Set the color of the legend text to red and set the background color of the legend to yellow.
```python
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
legend = plt.legend()
plt.setp(legend.get_texts(), color='r')
legend.get_frame().set_facecolor('yellow')
plt.show()
```

Add a border to the legend with a line width of 5.
```python
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
legend = plt.legend()
legend.get_frame().set_linewidth(5.0)
plt.show()
```

Set the opacity of the legend to 0.5.
```python
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
legend = plt.legend()
legend.get_frame().set_alpha(0.5)
plt.show()
```