---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: iris Dataset
  difficulty: Easy
  module: pandas
  idx: 45
  num_steps: 5
  step_types:
    - exec
    - vis
    - text
    - text
    - text
  modules:
    - pandas
    - pandas&matplotlib
    - pandas
    - pandas
    - pandas
---

File Path: `data/iris.csv`

Load the dataset from the path. Assign names to the columns as 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', and 'class'. Drop the first row.
```python
import pandas as pd

url = 'data/iris.csv'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv(url, names=names)
df = df.drop(df.index[0])
```


Create a scatter plot between 'sepal-length' and 'sepal-width' with 'sepal-length' on the x-axis and 'sepal-width' on the y-axis.
```python
import matplotlib.pyplot as plt 
plt.scatter(df['sepal-length'], df['sepal-width'])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
```

Convert the 'class' column to the category data type. Display the dataframe.
```python
df['class'] = df['class'].astype('category')
df.dtypes
```

Filter the rows where 'sepal-length' is greater than the mean 'sepal-length'. Display the dataframe.
```python
df['sepal-length'] = df['sepal-length'].astype('float')
mean_sepal_length = df['sepal-length'].mean()
df_filtered = df[df['sepal-length'] > mean_sepal_length]
df_filtered
```

Finally, sort the dataframe in descending order of 'sepal-length'. Display the dataframe.
```python
df_sorted = df.sort_values('sepal-length', ascending=False)
df_sorted
```