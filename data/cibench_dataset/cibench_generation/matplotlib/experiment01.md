---
jupyter:
  title: Creating and Displaying Sin and Cos Plots using Matplotlib in Python
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 1
  num_steps: 5
  step_types:
    - vis
    - vis
    - exec
    - vis
    - vis
  modules: 
    - numpy & matplotlib 
    - numpy & matplotlib 
    - numpy & matplotlib
    - numpy & matplotlib
    - numpy & matplotlib
---

Generate the data required for plotting. Here, you will be creating a sine wave and a cosine wave. Define a range of x values from 0 to 2*pi, and calculate the corresponding y values as sin(x) and cos(x).Then create a new figure with two subplots. This will allow you to plot multiple data series in the same figure.

```python
import numpy as np
x = np.linspace(0, 2*np.pi, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 1)
```

Plot the sine wave on the first subplot (`ax[0]`) and the cosine wave on the second subplot (`ax[1]`). You can change the style and color of your plot lines. For example, use 'r--' for a red dashed line and 'g-' for a green solid line. 

```python
ax[0].plot(x, y_sin, 'r--')
ax[1].plot(x, y_cos, 'g-')
```

Customize your subplots by adding titles, labels, and a grid. This will make the plots more readable and informative. 

```python
ax[0].set_title('Sine Wave')
ax[0].set_xlabel('x')
ax[0].set_ylabel('sin(x)')
ax[0].set_xlim([0, 2*np.pi])
ax[0].grid(True)

ax[1].set_title('Cosine Wave')
ax[1].set_xlabel('x')
ax[1].set_ylabel('cos(x)')
ax[1].set_xlim([0, 2*np.pi])
ax[1].grid(True)
```

Add a legend to your plots to provide information about the data series. Here, use the labels 'sin(x)' for the sine wave and 'cos(x)' for the cosine wave. Then display your plots with the `show()` function.

```python
ax[0].legend(['sin(x)'])
ax[1].legend(['cos(x)'])
plt.show()
```

If you want to provide additional information, you can add text to your plots. For example, you can add the text 'Text in the middle' in the middle of the first subplot.

```python
ax[0].text(0.5, 0.5, 'Text in the middle', transform=ax[0].transAxes)
plt.show()
```