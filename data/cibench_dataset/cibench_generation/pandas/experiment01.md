---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Iris dataset
  difficulty: Easy
  module: pandas
  idx: 1
  num_steps: 6
  step_types:
    - exec
    - text
    - num
    - num
    - num
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - matplotlib
---

File Path: `data/iris.csv`

Load the Iris dataset from the path into a DataFrame using the pandas library.
```python
import pandas as pd
data = pd.read_csv('data/iris.csv')
data.head()
```

Get the number of rows and columns in the dataset.
```python
data.shape
```

Check for null values in the dataset. Display sum of the number of null values in each column.
```python
data.isnull().sum().sum()
```

Find the unique elements of the 'species' column. Display the number of unique values.
```python
# display number
len(data['species'].unique())
```

Count the number of rows for each unique value of the 'species' column. Display the count of setosa.
```python
data['species'].value_counts()['setosa']
```

Plot a histogram of the 'sepal_length' column.
```python
import matplotlib.pyplot as plt

data['sepal_length'].hist(bins=30)
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.show()
```
