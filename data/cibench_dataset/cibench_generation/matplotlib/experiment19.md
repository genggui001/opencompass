---
jupyter:
  title: Visualizing Synthetic Data Using Numpy and Matplotlib
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 19
  num_steps: 7
  step_types:
    - vis
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
    - numpy & matplotlib
    - numpy & matplotlib
    - numpy & matplotlib
---

Generate an array of 100 evenly spaced numbers between 0 and 10. Compute the cosine of the numbers and plot the result. Add a title "Cosine function" to the plot and label the x-axis as "x" and y-axis as "cos(x)".
```python
import numpy as np
x = np.linspace(0, 10, 100)
y = np.cos(x)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.title("Cosine function")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.show()
```

Change the plot line to be dashed and red.Add a legend to the plot with the label 'cos(x)'.Compute the sine of the numbers and plot it with dashed blue line. Plot the cosine and sine functions on the same plot.
```python
y2 = np.sin(x)
plt.plot(x, y, linestyle='--', color='red', label='cos(x)')
plt.plot(x, y2, linestyle='-', color='blue', label='sin(x)')
plt.title("Cosine and Sine functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
```

Create two subplots – the cosine function in the first subplot and the sine function in the second subplot.
```python
plt.subplot(2, 1, 1)
plt.plot(x, y, linestyle='--', color='red', label='cos(x)')
plt.title("Cosine function")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x, y2, linestyle='-', color='blue', label='sin(x)')
plt.title("Sine function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.tight_layout()
plt.show()
```

Generate two arrays of 50 random numbers. Create a scatter plot of these random numbers.Change the size of the markers in the scatter plot to 100 and their color to red.
```python
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, s=100, color='red')
plt.title("Scatter plot")
plt.show()
```

Generate an array of 1000 normally distributed random numbers. Create a histogram of these numbers with 30 bins.Change the color of the histogram to green and the edge color to black.
```python
x = np.random.randn(1000)
plt.hist(x, bins=30, color='green', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

Generate an array of 100 random integers between 0 and 10. Create a bar plot of the frequency of these numbers.Change the color of the bars in the bar plot to orange and the edge color to black.
```python
x = np.random.randint(0, 10, 100)
counts = np.bincount(x)
plt.bar(range(10), counts, color='orange', edgecolor='black')
plt.title("Bar plot")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

Create a pie chart of the frequencies of the numbers above."Explode" the largest slice in the pie chart.
```python
explode = [0.1 if i == counts.argmax() else 0 for i in range(10)]
plt.pie(counts, labels=range(10), autopct='%1.1f%%', explode=explode)
plt.title("Pie chart")
plt.show()
```