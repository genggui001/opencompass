---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Iris Dataset
  difficulty: Easy
  module: pandas
  idx: 2
  num_steps: 6
  step_types:
    - exec
    - text
    - num
    - num
    - num
    - num
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---

File Path: `data/iris.csv`

Load the Iris dataset.

```python
import pandas as pd

df = pd.read_csv('data/iris.csv')
df.head()
```

Print the data types of each column in the dataframe.

```python
df.dtypes
```

Group the data by 'species' and calculate the mean of the other columns. Display the multiplication of sepal_length mean of setosa and sepal_width mean of setosa. Keep to 2 decimal places. 

```python
grouped = df.groupby('species').mean()
round(grouped.iloc[0,0] * grouped.iloc[0,1], 2)
```

Filter the data to display only rows where 'sepal_length' is greater than 6.3 using boolean indexing. Display the number of rows in the filtered dataframe.

```python
len(df[df['sepal_length'] > 6.3])
```

Sort the data by 'sepal_length' in descending order. Print the index of the first sorted row.

```python
sorted_df = df.sort_values('sepal_length', ascending=False)
sorted_df.iloc[0].name
```

Add a new column 'sepal_area' to the dataframe, which is the product of 'sepal_length' and 'sepal_width'. Display the second value of the new column. Keep to 2 decimal places.

```python
df['sepal_area'] = df['sepal_length'] * df['sepal_width']
df['sepal_area'][1].round(2)
```