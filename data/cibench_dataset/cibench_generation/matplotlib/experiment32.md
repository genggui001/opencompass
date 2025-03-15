---
jupyter:
  title: Visualize the iris dataset with histograms, scatter plots, box plots, line plots, and pie charts.
  module: matplotlib
  dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
  difficulty: MIDDLE
  idx: 32
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - pandas
    - matplotlib
    - matplotlib
    - matplotlib
---

File Path: "data/matplotlib_dataset05_iris.data".

Load the Iris dataset from path. Assign names to the columns as 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', and 'class'.
```python
url = "data/matplotlib_dataset05_iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
import pandas as pd
dataset = pd.read_csv(url, names=names)
```

Generate a scatter plot to visualize the relationship between sepal length and sepal width. Assign different colors to different classes in the scatter plot using a dictionary.
```python
import matplotlib.pyplot as plt
colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}
plt.scatter(dataset['sepal-length'], dataset['sepal-width'], c=dataset['class'].apply(lambda x: colors[x]))
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Width')
plt.show()
```

Create subplots to visualize multiple plots in one figure. Plot 1 line plot Sepal Length vs Width. Plot 2 hist plot of Sepal Length. Plot 3 Scatter plot of Sepal Length vs Width. Plot 4 Box plot of Sepal Length.
```python
fig, axes = plt.subplots(2, 2, figsize=(12,8))
axes[0, 0].plot(dataset['sepal-length'], dataset['sepal-width'])
axes[0, 0].set_title('Sepal Length vs Width')
axes[0, 1].hist(dataset['sepal-length'])
axes[0, 1].set_title('Histogram of Sepal Length')
axes[1, 0].scatter(dataset['sepal-length'], dataset['sepal-width'])
axes[1, 0].set_title('Scatter plot of Sepal Length vs Width')
axes[1, 1].boxplot(dataset['sepal-length'])
axes[1, 1].set_title('Box plot of Sepal Length')
plt.tight_layout()
plt.show()
```

Use a bar plot to compare the frequency of each class in the dataset.
```python
dataset['class'].value_counts().plot.bar()
plt.title('Frequency of Iris classes')
plt.show()
```