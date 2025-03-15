---
jupyter:
  title: Creating and Displaying Different Types of Plots using Matplotlib in Python
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 0
  num_steps: 6
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - none
    - matplotlib 
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

Generate a list of integers from 1 to 5 that will be used for plotting.
```python
data = [1, 2, 3, 4, 5]
```

Plot the generated list with red dash line.
```python
import matplotlib.pyplot as plt
plt.plot(data, 'r--')
plt.title('My First Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()
```

Generate another list of integers from 5 to 1. Use blue solid line. Plot both line in one figure.
```python
data2 = [5, 4, 3, 2, 1]
plt.plot(data, 'r--', data2, 'b-')
plt.title('My First Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()
```

Create a scatter plot using the two lists of integers. The first list is used as the x-values and the second list is used as the y-values.
```python
plt.scatter(data, data2)
plt.title('My First Scatter Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()
```

Generate a histogram of the first list of integers using the hist function. The bins parameter is set to 5. The alpha parameter is set to 0.5.
```python
plt.hist(data, bins=5, alpha=0.5)
plt.title('My First Histogram')
plt.xlabel('X-Axis')
plt.ylabel('Frequency')
plt.show()
```

Lastly, create a boxplot of the first list of integers using the boxplot function.
```python
plt.boxplot(data)
plt.title('My First Boxplot')
plt.show()
```