---
jupyter:
  title: Applying and Creating Styles in Matplotlib 
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 11
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

Create a Sine Wave from 0-10 with 100 intervals.
```python
import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y)
plt.show()
```

Apply classic Styles.
```python
plt.style.use('classic')
plt.plot(X, Y)
plt.show()
```

Now, let's try the 'ggplot' style.
```python
plt.style.use('ggplot')
plt.plot(X, Y)
plt.show()
```

Merge Multiple Styles 'ggplot' and 'bmh'.
```python
plt.style.use(['ggplot', 'bmh'])
plt.plot(X, Y)
plt.show()
```

Create Your Own Style then reset to the Default Style
```python
style = {'figure.facecolor': 'white',
         'axes.facecolor': 'lightgray',
         'axes.edgecolor': 'gray',
         'axes.grid': True,
         'grid.color': 'white'}
plt.rcParams.update(style)
plt.plot(X, Y)
plt.show()
```

Convert Your Style from a String
```python
style = """
figure.facecolor: white
axes.facecolor: lightgray
axes.edgecolor: gray
axes.grid: True
grid.color: white
"""
style_dict = dict([line.split(': ') for line in style.split('\n') if line])
plt.rcParams.update(style_dict)
plt.plot(X, Y)
plt.show()
```