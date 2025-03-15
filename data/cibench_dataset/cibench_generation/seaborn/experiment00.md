---
jupyter:
  title: Analyzing Titanic Passenger Data
  module: seaborn
  dataset: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv
  difficulty: EASY
  idx: 0
  num_steps: 7
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - pandas
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
---

File Path: 'data/seaborn_titanic.csv'. 


Load the Titanic dataset into a pandas DataFrame.
```python
import pandas as pd
data = pd.read_csv('data/seaborn_titanic.csv')
```

Create a countplot to visualize the count of survivors with respect to gender.
```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x='survived', hue='sex', data=data)
plt.show()
```

Use a barplot to visualize the average age of passengers who survived and who didn't survive.
```python
sns.barplot(x='survived', y='age', data=data)
plt.show()
```

Create a boxplot to visualize the age distribution with respect to passenger class.
```python
sns.boxplot(x='pclass', y='age', data=data)
plt.show()
```

Use a pairplot to visualize pairwise relationships in the dataset.
```python
sns.pairplot(data)
plt.show()
```

Create a violinplot to visualize the age distribution with respect to passenger class and gender.
```python
sns.violinplot(x='pclass', y='age', hue='sex', data=data, split=True)
plt.show()
```

Finally, create a jointplot to visualize the relationship between age and fare.
```python
sns.jointplot(x='age', y='fare', data=data)
plt.show()
```
