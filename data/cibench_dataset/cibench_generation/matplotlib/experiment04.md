---
jupyter:
  title: Plotting Sine, Cosine, Tangent and Hyperbolic Sine Functions with Matplotlib and Numpy
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 4
  num_steps: 5
  step_types:
    - vis
    - vis
    - vis
    - vis
    - exec
  modules: 
    - numpy & matplotlib 
    - numpy & matplotlib
    - numpy & matplotlib
    - numpy & matplotlib
    - numpy & matplotlib
---

The numpy library is used to generate a range of values from 0 to 4*pi with 1000 values, which we will use as x-values for plotting our functions. Plot a Sine Wave.
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4 * np.pi, 1000)
plt.plot(x, np.sin(x))
plt.show()
```

Plot a Sine and Cosine Wave Together We can add a cosine wave to the same plot as the sine wave.Then add Labels, Title, and Legend to the Plot.
Adding labels to the x and y axis, a title to the plot and legends to the graphs.
```python
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x) and cos(x)')
plt.legend()
plt.show()
```

Create 2x2 subplots in a single figure, for sine, cosine, tangent, hyperbolic sine waves, and adjust the size of the figure to 10 inches by 6 inches.
```python
fig, axs = plt.subplots(2, 2, figsize=(10, 6))

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('sin(x)')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('cos(x)')

axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title('tan(x)')

axs[1, 1].plot(x, np.sinh(x))
axs[1, 1].set_title('sinh(x)')

plt.tight_layout()
plt.show()
```


Plot an Exponential Function with a Logarithmic y-scale
We can set the y-scale of the first subplot to log and plot an exponential function in it. In the second subplot, we plot a sine function:
```python
fig, axs = plt.subplots(2, figsize=(10, 6))

axs[0].plot(x, np.exp(x))
axs[0].set_title('exp(x)')
axs[0].set_yscale('log')

axs[1].plot(x, np.sin(x))
axs[1].set_title('sin(x)')

plt.tight_layout()
plt.show()
```

Finally, we can add a customized grid with red color, dashed style and width of 0.5 to a sine wave plot.
```python
plt.plot(x, np.sin(x))
plt.title('sin(x)')
plt.grid(color='red', linestyle='--', linewidth=0.5)
plt.show()
```
