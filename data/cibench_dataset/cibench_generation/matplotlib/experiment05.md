---
jupyter:
  title: Exploring and Visualizing the Iris Dataset with Pandas and Matplotlib
  module: matplotlib
  dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
  difficulty: EASY
  idx: 5
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - pandas 
    - pandas & matplotlib
    - pandas & matplotlib
    - pandas & matplotlib
    - pandas & matplotlib
---

File Path: data/matplotlib_dataset05_iris.data

Load the Iris dataset from path. Use names of 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'.
```python
import pandas as pd
url = "data/matplotlib_dataset05_iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
dataset.head()
```

Create a histogram for the 'sepal-length' column. Use 10 bins for this histogram and adding a title, x-axis label, and y-axis label.
```python
import matplotlib.pyplot as plt
plt.hist(dataset['sepal-length'], bins=10)
plt.title('Sepal Length Histogram')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()
```

Create a box plot for the 'sepal-width' column.
```python
plt.boxplot(dataset['sepal-width'])
plt.show()
```

Create a box plot for each column in the dataset.
```python
dataset.boxplot()
plt.show()
```

Create a histogram for each column in the dataset and adjust the layout of the histogram to prevent overlapping.many features.
```python
dataset.hist()
plt.tight_layout()
plt.show()
```