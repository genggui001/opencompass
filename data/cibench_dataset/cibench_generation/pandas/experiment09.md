---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Titanic dataset
  difficulty: Easy
  module: pandas
  idx: 9
  num_steps: 5
  step_types:
    - exec
    - num
    - text
    - num
    - num
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---

File Path: `data/titanic.csv`

Load the Titanic dataset into a pandas DataFrame using pandas function.
```python
import pandas as pd
url = 'data/titanic.csv'
df = pd.read_csv(url)
```

Identify how many values are missing in each column of the DataFrame. Display the number of all missing values.
```python
df.isnull().sum().sum()
```

Remove 'Cabin' Column. The 'inplace' parameter is set to True to make the change permanent. Check if the column has been removed.
```python
df.drop('Cabin', axis=1, inplace=True)
'Cabin' in df.columns
```

Replace the missing values in the 'Age' column with the median age value. Display the number of missing values in 'Age'.
```python
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Age'].isnull().sum()
```

Change the values in the 'Sex' column from 'male' and 'female' to 0 and 1 respectively to facilitate further analysis. Display the difference between number of male and females.
```python
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
abs(len(df[df['Sex'] == 0]) - len(df[df['Sex'] == 1]))
```
