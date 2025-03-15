---
jupyter:
  title: Generating Basic Plots with Matplotlib including Line, Bar, and Scatter Plots
  module: matplotlib
  dataset: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'.
  difficulty: MIDDLE
  idx: 2
  num_steps: 5
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - pandas & matplotlib 
    - pandas & matplotlib
    - pandas & matplotlib
    - pandas & matplotlib
    - pandas & matplotlib
---

File Path: 'data/matplotlib_dataset02_iris.csv'.

Load the Iris dataset into a pandas DataFrame using the read_csv function.Then Generate a line plot with 'sepal_length' on the x-axis and 'sepal_width' on the y-axis. Use the color of the line to red and the line style to dashed.

```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/matplotlib_dataset02_iris.csv')
plt.plot(df['sepal_length'], df['sepal_width'], color='red', linestyle='dashed')
plt.show()
```

Use the bar() function of matplotlib, with the indices of the value_counts() of 'species' as the x-values and the values of the value_counts() as the y-values.

```python
plt.bar(df['species'].value_counts().index, df['species'].value_counts().values)
plt.show()
```

Generate a scatter plot with 'sepal_length' on the x-axis and 'sepal_width' on the y-axis with the marker style to 'x' and the color to 'red'.

```python
plt.scatter(df['sepal_length'], df['sepal_width'], marker='x', color='red')
plt.show()
```

Generate a histogram for 'sepal_length' using the hist() function of matplotlib. Set the number of bins to 10 by passing 10 to the bins parameter. With the color of the histogram to purple and add a black edge color. 

```python
plt.hist(df['sepal_length'], bins=10, color='purple', edgecolor='black')
plt.show()
```

Use the boxplot() function of pandas, passing 'sepal_length' to the column parameter and 'species' to the by parameter.

```python
df.boxplot(column='sepal_length', by='species')
plt.show()
```
