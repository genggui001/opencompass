---
jupyter:
  title: Loads and analyzes the iris dataset using pandas and matplotlib, and creates various visualizations
  module: matplotlib
  dataset: "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
  difficulty: EASY
  idx: 14
  num_steps: 6
  step_types:
    - exec
    - vis
    - vis
    - vis  
    - vis
    - vis
  modules: 
    - pandas
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

File Path: "data/matplotlib_dataset05_iris.data".

Load the iris dataset.Use names of 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'.
```python
url = "data/matplotlib_dataset05_iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
import pandas as pd
df = pd.read_csv(url, names=names)
df.head()
```

Visualize the relationship between 'sepal-length' and 'sepal-width' with a scatter plot.
```python
import matplotlib.pyplot as plt
df.plot(kind='scatter',x='sepal-length',y='sepal-width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
```

Compare the mean 'sepal-length' of each class using a bar chart.
```python
df.groupby('class')['sepal-length'].mean().plot(kind='bar')
plt.ylabel('Mean Sepal Length')
plt.show()
```

Create a scatter matrix plot for all numerical columns to understand the correlation between each pair of features.
```python
pd.plotting.scatter_matrix(df)
plt.show()
```

Create a time series plot using 'sepal-length' and 'sepal-width' for the first 50 rows.
```python
df[['sepal-length', 'sepal-width']][:50].plot()
plt.ylabel('Measurement')
plt.show()
```

Create a scatter plot with 'petal-length' and 'petal-width' colored by 'class'.
```python
colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}
plt.scatter(df['petal-length'], df['petal-width'], c=df['class'].apply(lambda x: colors[x]))
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()
```