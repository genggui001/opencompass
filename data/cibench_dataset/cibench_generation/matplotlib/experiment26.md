---
jupyter:
  title: Customizing ticks on a basic sine wave plot using matplotlib and numpy
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 26
  num_steps: 5
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - matplotlib & numpy
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

Generate 1000 values between 0 and 10. Calculate the sine of these values to get the y coordinates. Plot these coordinates and set the ticks at the values 0, 2, 4, 6, 8, and 10 on the x-axis. Set the ticks at the values -1, 0, and 1 on the y-axis.
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.xticks([0, 2, 4, 6, 8, 10])
plt.yticks([-1, 0, 1])
plt.show()
```

Set the ticks at the values 0, 2, 4, 6, 8, and 10 on the x-axis. Set the ticks at the values -1, 0, and 1 on the y-axis.
```python
plt.plot(x, y)
plt.xticks([0, 2, 4, 6, 8, 10])
plt.yticks([-1, 0, 1])
plt.show()
```

Replace the numerical tick labels on both axes with textual labels and rotate the x-axis labels by 45 degrees and the y-axis labels by 30 degrees.
```python
plt.plot(x, y)
plt.xticks([0, 2, 4, 6, 8, 10], ['zero', 'two', 'four', 'six', 'eight', 'ten'], rotation=45)
plt.yticks([-1, 0, 1], ['negative one', 'zero', 'one'], rotation=30)
plt.show()
```

Set the font size of ticks to 12. Set the direction to 'inout', which means the ticks will extend in both inward and outward directions.
```python
plt.plot(x, y)
plt.xticks([0, 2, 4, 6, 8, 10], ['zero', 'two', 'four', 'six', 'eight', 'ten'], rotation=45, fontsize=12)
plt.yticks([-1, 0, 1], ['negative one', 'zero', 'one'], rotation=30, fontsize=12)
plt.tick_params(axis='both', direction='inout')
plt.show()
```

Set bottom, top, right, and left to False to hide the ticks, and set labelbottom and labelleft to False to hide the tick labels.
```python
plt.plot(x, y)
plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
plt.show()
```
