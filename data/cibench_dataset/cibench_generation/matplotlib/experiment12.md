---
jupyter:
  title: Exploring Iris Dataset with Line and Bar Graphs 
  module: matplotlib
  dataset: none
  difficulty: EASY
  idx: 12
  num_steps: 4
  step_types:
    - vis
    - vis
    - vis
    - vis
  modules: 
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

File Path: 'data/matplotlib_dataset02_iris.csv'.

Generate an array of 100 numbers between 0 and 10 using numpy's linspace function. Add random errors to the sin values and plot errorbar.
```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
dy = 0.1
y = np.sin(x) + dy * np.random.randn(100)
plt.errorbar(x, y, yerr=dy, fmt='.k')
plt.show()
```

Modify the error bars to make them less obtrusive. Change their color to light gray and increase their line width.
```python
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)
plt.show()
```

Load data from path. Compute the mean and standard deviation of the 'sepal_length' for each species using pandas' groupby, mean, and std functions.Create a bar plot of the mean 'sepal_length' for each species. Use the standard deviation as error bars, and label the axes and the plot.
```python
import pandas as pd
data = pd.read_csv('data/matplotlib_dataset02_iris.csv')
means = data.groupby('species')['sepal_length'].mean()
stds = data.groupby('species')['sepal_length'].std()
plt.bar(means.index, means.values, yerr=stds.values, capsize=10)
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Mean Sepal Length of Iris Species')
plt.show()
```

Add labels to the bars displaying the mean values rounded to two decimal places using matplotlib's text function.Define a function that takes a DataFrame, a category column, a value column, and an aggregation method (either 'mean' or 'median'). This function creates a bar plot of the aggregated values with error bars for each category.
Use the above function to create bar plots for 'sepal_length' and use 'median' as aggregation methods.
```python
for i, v in enumerate(means.values):
    plt.text(i, v+0.1, round(v, 2), ha='center')
def plot_with_errorbars(df, cat_col, val_col, agg_method):
    if agg_method == 'mean':
        vals = df.groupby(cat_col)[val_col].mean()
        errs = df.groupby(cat_col)[val_col].std()
    elif agg_method == 'median':
        vals = df.groupby(cat_col)[val_col].median()
        errs = df.groupby(cat_col)[val_col].mad()
    plt.bar(vals.index, vals.values, yerr=errs.values, capsize=10)
    plt.xlabel(cat_col)
    plt.ylabel(val_col)
    plt.title(f'{agg_method.capitalize()} {val_col} of {cat_col}')
    for i, v in enumerate(vals.values):
        plt.text(i, v+0.1, round(v, 2), ha='center')
plot_with_errorbars(data, 'species', 'sepal_length', 'median')
plt.show()
```
