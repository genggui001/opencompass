---
jupyter:
  title: Dataset processing using pandas in Python
  dataset: Titanic
  difficulty: Easy
  module: pandas
  idx: 0
  num_steps: 5
  step_types:
    - exec
    - num
    - vis
    - num
    - num
  modules:
    - pandas
    - pandas
    - matplotlib
    - pandas
    - pandas
---

File Path: `data/titanic.csv`

Load the Titanic dataset from path into a DataFrame. Preview the DataFrame to understand its structure. Display the first 5 rows.

```python
import pandas as pd

path = 'data/titanic.csv'
data = pd.read_csv(path)
data.head()
```

Check for missing values in the dataset. Display the sum of number of missing values in each column.

```python
data.isna().sum().sum()
```

Analyse the 'Survived' column. Count the number of survivors and non-survivors. Visualize the count of survivors using a bar plot.[Title](experiment24.md)

```python
import matplotlib.pyplot as plt

data['Survived'].value_counts()
data['Survived'].value_counts().plot(kind='bar')
plt.show()
```

Group the data by 'Pclass' and 'Survived'. Get the count of each group. Display the value of the group with 'Pclass' = 1 and 'Survived' = 0.

```python
data.groupby(['Pclass', 'Survived']).size()[1, 0]
```

Handle the missing values in the 'Age' column. Replace the missing values with the median of 'Age' column. Make the change permanent by setting 'inplace' to True. Display the sum of number of missing values in each column.

```python
data['Age'].fillna(data['Age'].median(), inplace=True)
data.isna().sum().sum()
```