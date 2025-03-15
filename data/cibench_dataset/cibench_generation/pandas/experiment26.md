---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: titanic Dataset
  difficulty: Easy
  module: pandas
  idx: 26
  num_steps: 5
  step_types:
    - exec
    - text
    - text
    - num
    - text
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---

File Path: `data/titanic.csv`

Load the Titanic dataset from the provided pathusing pandas' read_csv() function.
```python
import pandas as pd
url = 'data/titanic.csv'
data = pd.read_csv(url)
data.head()
```

Convert the 'Sex' column to a category data type using the astype() function. Verify the conversion by displaying the data types of all columns. Verify if the 'Sex' column is of category data type.
```python
data['Sex'] = data['Sex'].astype('category')
data['Sex'].dtype.name == 'category'
```

Convert the 'Age' column into a categorical column named 'AgeGroup' with 10-year intervals, named as '0-10', '10-20', etc. Display the first two rows of the dataset to verify the operation.
```python
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)
data.head(2)
```

Count the number of occurrences of each category in the 'AgeGroup' column. Display the result of 20-30.
```python
data['AgeGroup'].value_counts()['20-30']
```

Add a new category 'Unknown' to the 'Embarked' column and replace missing values with 'Unknown'. Display the categories of the 'Embarked' column to verify the operation.
```python
data['Embarked'] = data['Embarked'].astype('category')
data['Embarked'] = data['Embarked'].cat.add_categories(['Unknown'])
data['Embarked'].fillna('Unknown', inplace=True)
data['Embarked'].cat.categories
```
