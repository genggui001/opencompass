---
jupyter:
  title: Visualizing and Comparing Sine and Cosine Waves using Python
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 30
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - numpy
    - matplotlib
    - matplotlib
    - matplotlib & numpy
---

Create an array of 500 evenly spaced values between 0 and 10. Then use these x-values to generate y-values for both sine and cosine functions.
```python
import numpy as np
x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)
```

Plot both lines. Use blue color for the sine plot and red color for the cosine plot. Add labels to each plot and display a legend in the upper right corner. Also, label your x-axis as 'x' and y-axis as 'y'. Add a title to your plot as 'Sine and Cosine Waves'.
```python
import matplotlib.pyplot as plt
plt.plot(x, y1, '-b', label='sine')
plt.plot(x, y2, '-r', label='cosine')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Waves')
plt.show()
```

Fill the area between the sine and cosine curves. Set the fill color to purple and the transparency to 0.1.
```python
plt.plot(x, y1, '-b', label='sine')
plt.plot(x, y2, '-r', label='cosine')
plt.fill_between(x, y1, y2, color='purple', alpha=0.1)
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Waves with Filled Area')
plt.show()
```

Generate a new set of y-values for two different sine functions. Use the same x-values as before. generate y-values for both sine and sine+0.5 functions.
Fill the area between the two new sine curves. Set the fill color to red and the transparency to 0.1. 
```python
y1 = np.sin(x)
y2 = np.sin(x) + 0.5
plt.plot(x, y1, '-b', label='sin(x)')
plt.plot(x, y2, '-r', label='sin(x) + 0.5')
plt.fill_between(x, y1, y2, color='red', alpha=0.1)
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x) and sin(x) + 0.5 with Filled Area')
plt.show()
```