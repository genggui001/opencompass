---
jupyter:
  title: Exploring Different Plot Scales Using Matplotlib and Numpy.
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 41
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy
    - matplotlib
    - matplotlib
    - matplotlib
    - numpy & matplotlib
---

Generate a sequence of 400 evenly spaced values between 0 and 10 using the Numpy linspace function. Store this sequence in a variable 'x'.Create a new sequence y = x^2.
```python
import numpy as np
x = np.linspace(0, 10, 400)
y = x**2
```

Create a plot of 'y' against 'x' where the x-axis is on a logarithmic scale adding a title to the plot and labels to both the x-axis and y-axis.
```python
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xscale('log')
plt.title('Logarithmic x-axis')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

Create two subplots in the same figure. The first subplot should plot 'y' against 'x' on a linear scale and the second subplot should plot 'y' against 'x' on a logarithmic scale.
```python
fig, axs = plt.subplots(2)
fig.suptitle('Linear vs Logarithmic')
axs[0].plot(x, y)
axs[0].set_title('Linear scale')
axs[1].semilogy(x, y)
axs[1].set_title('Logarithmic scale')
plt.show()
```

Generate two subplots in the same figure. The first subplot should plot 'y' against 'x' with the y-axis on a base 10 logarithmic scale. The second subplot should plot 'y' against 'x' with the y-axis on a base 2 logarithmic scale.
```python
fig, axs = plt.subplots(2)
fig.suptitle('Base 10 vs Base 2')
axs[0].semilogy(x, y)
axs[0].set_title('Base 10')
axs[1].semilogy(x, y, 2)
axs[1].set_title('Base 2')
plt.show()
```

Create a new sequence 'y' by applying the sine function to each value in the 'x' sequence. Plot this new sequence against 'x'. Transform the y-axis to a logarithmic scale and transform the y-axis to a symmetrical logarithmic scale.
```python
y = np.sin(x)
plt.semilogy(x, y)
plt.yscale('symlog')
plt.show()
```