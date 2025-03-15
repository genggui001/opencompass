---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: titanic Dataset
  difficulty: Easy
  module: pandas
  idx: 22
  num_steps: 6
  step_types:
    - exec
    - exec
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
    - pandas&matplotlib
---


File Path: `data/titanic.csv`


Load the Titanic dataset from the provided path. This dataset is in CSV format.

```python
import pandas as pd
data = pd.read_csv('data/titanic.csv')
data.head()
```

Extract the title from the 'Name' column.  Store the extracted titles in a new column named 'Title'.
```python
data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
data.head()
```

Standardize the 'Title' column by replacing all titles that are not 'Mr', 'Miss', 'Mrs', and 'Master' with 'Other'. Display total number of Other.
```python
titles = ['Mr', 'Miss', 'Mrs', 'Master']
data['Title'] = data['Title'].replace([x for x in data['Title'].unique().tolist() if x not in titles], 'Other')
len(data[data['Title'] == 'Other'])
```

Create a new column 'FamilySize' by adding the 'SibSp' (number of siblings/spouses aboard) and 'Parch' (number of parents/children aboard) columns. This will give a total count of family members aboard for each passenger. Display the sum of total famuly size.
```python 
data['FamilySize'] = data['SibSp'] + data['Parch']
data['FamilySize'].sum()
```

Calculate the survival rate by family size by grouping the data by 'FamilySize' and taking the mean of the 'Survived' column. Display the mean of family size 0. Keep to 2 decimal places.
```python
round(data.groupby('FamilySize')['Survived'].mean()[0], 2)
```

Visualize the survival rate by family size using a bar plot.
```python
import matplotlib.pyplot as plt
data.groupby('FamilySize')['Survived'].mean().plot(kind='bar')
plt.show()
```