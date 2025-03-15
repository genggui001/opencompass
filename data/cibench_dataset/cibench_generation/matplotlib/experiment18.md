---
jupyter:
  title: Creating and Modifying Polar Plots using Matplotlib and Numpy in Python
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 18
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
    - matplotlib
    - matplotlib
    - numpy & matplotlib
    - matplotlib
    - numpy & matplotlib
---

Generate a range of numbers from 0-2 as the radius for the polar plot.Create an array of angles by multiplying the range by 2*pi. This will be used as the theta (angle) for the polar plot.Plot the generated angles against the range.
```python
import numpy as np
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
import matplotlib.pyplot as plt
plt.polar(theta, r)
plt.title("A simple polar plot")
plt.show()
```

Change the color of the plot to red. Add gridlines.
```python
plt.polar(theta, r, color='r')
plt.title("A simple polar plot with changed color")
plt.grid(True)
plt.show()
```

Reverse the direction of your plot and move the zero location of your plot to 45 degrees.
```python
ax = plt.subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 4)
ax.plot(theta, r, color='r')
plt.title("Polar plot with changed zero location")
plt.show()
```

Create a polar bar plot. First, generate an array of radii and widths using numpy's "random" function. Then create a bar subplot with polar projection.
```python
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
ax = plt.subplot(111, polar=True)
bars = ax.bar(theta, radii, width=width)
plt.show()
```

Add different colors to the bars in your plot.Add labels to your polar plot.
```python
ax = plt.subplot(111, polar=True)
bars = ax.bar(theta, radii, width=width)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
plt.show()
```

Generate a polar scatter plot. Begin by creating arrays of radii, angles, areas, and colors use random number. Then, create a sactter subplot with polar projection.
```python
N = 50
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
ax = plt.subplot(111, polar=True)
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
plt.show()
```