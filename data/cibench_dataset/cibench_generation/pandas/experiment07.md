---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Pima Indians Diabetes dataset
  difficulty: Easy
  module: pandas
  idx: 7
  num_steps: 6
  step_types:
    - exec
    - text
    - num
    - num
    - num
    - text
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---
File Path: `data/pima-indians-diabetes.csv`

Load the Pima Indians Diabetes dataset from the provided path. Drop the first column.
```python
import pandas as pd
path = "data/pima-indians-diabetes.csv"
df = pd.read_csv(path)
df = df.drop(df.columns[0], axis=1)
```

Select the first four rows and first two columns from the dataset. Display the shape of the resulting DataFrame.
```python
df.iloc[0:4, 0:2].shape
```

Filter and display rows where 'age' is greater than 30 and 'class' is 1. Display the number of rows in the resulting DataFrame.
```python
len(df[(df['age'] > 30) & (df['class'] == 1)])
```

Group data by 'class' and calculate the mean of other columns. Keep to two decimal places by rounding the values. Display the value of preg in class 0.
```python
df.groupby('class').mean().round(2)["preg"][0]
```

Sort the data by 'age'. Print the index of the first sorted row.
```python
sorted_df = df.sort_values('age')
sorted_df.iloc[0].name
```

Create a new column 'age_class' which is the product of 'age' and 'class' on the sorted data. Display the two rows.
```python
sorted_df['age_class'] = sorted_df['age'] * sorted_df['class']
sorted_df.head(2)
```