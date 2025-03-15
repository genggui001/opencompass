---
jupyter:
  title: Data Analysis and Visualization of Iris Dataset
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 11
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - seaborn
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---


Load the Iris dataset from seaborn's in-built datasets.
```python
import seaborn as sns
iris = sns.load_dataset('iris')
```

Visualize the pairwise relationships between all variables in the dataset and distinguish the different flower species by color.
```python
import matplotlib.pyplot as plt
sns.pairplot(iris, hue='species')
plt.show()
```

Focus on the pairwise relationship between 'sepal_length' and 'sepal_width' variables. Fit a linear regression model to the scatterplots in the pairplot.
```python
sns.pairplot(iris, vars=['sepal_length','sepal_width'], kind='reg')
plt.show()
```

Change the diagonal plots in the pairplot to histograms. Alter the color palette of the pairplot to 'husl'. Customize the markers used in the pairplot by specifying a list of markers.
```python
sns.pairplot(iris, diag_kind='hist', palette='husl', markers=['D','s','D'])
plt.show()
```
