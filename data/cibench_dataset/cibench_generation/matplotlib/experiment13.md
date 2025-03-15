---
jupyter:
  title: Creating and Customizing Plots Using Matplotlib 
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 13
  num_steps: 3
  step_types:
    - vis
    - vis
    - vis
  modules: 
    - matplotlib
    - matplotlib
    - matplotlib
---

Generate the x values range from 0 to 9. Plot lines and label the lines as 'y=x' and 'y=x^2' respectively. Let's add the title 'My First Plot' to our plot.

```python
import matplotlib.pyplot as plt
x = range(10)
plt.plot(x, x, label='y=x')
plt.plot(x, [i**2 for i in x], label='y=x^2')
plt.title('My First Plot')
plt.show()
```

Add a legend on the upper center and turn off the frame. Let's annotate the point (2, 4) on our plot with the text 'Point (2,4)' and an arrow pointing to the point.
```python
plt.plot(x, x, label='y=x')
plt.plot(x, [i**2 for i in x], label='y=x^2')
plt.title('My First Plot')
plt.legend(loc='upper center', frameon=False)
plt.annotate('Point (2,4)', xy=(2, 4), xytext=(3, 20), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

Set the x and y axis limits and add grid lines to our plot. For the x-axis, the limits will be 0 and 10. For the y-axis, the limits will be 0 and 100.
```python
plt.plot(x, x, label='y=x')
plt.plot(x, [i**2 for i in x], label='y=x^2')
plt.title('My First Plot')
plt.legend(loc='upper center', frameon=False)
plt.annotate('Point (2,4)', xy=(2, 4), xytext=(3, 20), arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.grid(True)
plt.show()
```
