---
jupyter:
  title: Hierarchical Clustering Analysis of Iris Dataset Using Python
  module: SciPy
  dataset: data/scipy_dataset15.csv
  difficulty: EASY
  idx: 15
  num_steps: 9
  step_types:
    - num
    - vis
    - num
    - vis
  modules: 
    - pandas & scipy
    - scipy & matplotlib
    - scipy
    - matplotlib
---

File Path: data/scipy_dataset15.data.

Load the Iris dataset with name of ['sepal_length','sepal_width','petal_length','petal_width','target']. Drop the target column. Generate a linkage matrix from the feature data and use ward method. Display the len of matrix second dimension.
```python
import pandas as pd

df = pd.read_csv('data/scipy_dataset15.data', names=['sepal_length','sepal_width','petal_length','petal_width','target'])
data = df.drop('target', axis=1)
from scipy.cluster.hierarchy import linkage

Z = linkage(data, 'ward')

Z.shape[1]
```

Generate a dendrogram plot using the linkage matrix. The figure size is set to 10x7 for better visualization.
```python
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.show()
```

Form flat clusters from the hierarchical clustering defined by the given linkage matrix. The criterion is set to 'distance' and a maximum distance of 10 is used to form the clusters. Display the total number of unique clusters in clustering results.
```python
from scipy.cluster.hierarchy import fcluster

max_d = 10
clusters = fcluster(Z, max_d, criterion='distance')
len(set(clusters))
```

Plot a scatter diagram of the clusters using 'sepal_length' and 'sepal_width' as axes. The color of the points is determined by the cluster they belong to.
```python
plt.figure(figsize=(10, 7))
plt.scatter(df['sepal_length'], df['sepal_width'], c=clusters, cmap='prism')
plt.show()
```