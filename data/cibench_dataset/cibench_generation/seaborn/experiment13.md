---
jupyter:
  title: Visualizing the Iris Dataset Using Seaborn and Matplotlib
  module: seaborn
  dataset: none
  difficulty: MIDDLE
  idx: 13
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - seaborn
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---


Load the 'iris' dataset from seaborn's built-in datasets.
```python
import seaborn as sns
iris = sns.load_dataset('iris')
```

Calculate the correlation matrix of the iris dataframe. Create a heatmap of iris_corr using the seaborn heatmap function. Use a 'coolwarm' colormap and set annot to True to write the data value in each cell.
```python
import matplotlib.pyplot as plt
iris_corr = iris.corr()
sns.heatmap(iris_corr, cmap='coolwarm', annot=True)
plt.show()
```

Create a facet grid of histograms of 'sepal_length' for each species. Then, map a histogram to the grid.
```python
g = sns.FacetGrid(data=iris, col='species')
g.map(plt.hist, 'sepal_length')
plt.show()
```

Create a regression plot of 'sepal_length' and 'sepal_width'.
```python
sns.lmplot(x='sepal_length', y='sepal_width', data=iris)
plt.show()
```

Create a pair grid of all variables in the dataframe. Then, map histograms to the diagonal, scatter plots to the upper triangle, and kernel density estimates to the lower triangle. Create a rug plot of 'sepal_length'. Create a kernel density estimate plot of 'sepal_length'.
```python
g = sns.PairGrid(iris)
g.map_diag(sns.histplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
sns.rugplot(iris['sepal_length'])
sns.kdeplot(iris['sepal_length'])
plt.show()
```