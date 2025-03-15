---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: titanic Dataset
  difficulty: Easy
  module: pandas
  idx: 32
  num_steps: 6
  step_types:
    - exec
    - exec
    - text
    - vis
    - num
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
    - pandas
    - pandas&matplotlib
---

File Path: `data/titanic.csv`

Load the 'Titanic' dataset into a pandas DataFrame using the provided path.
```python
import pandas as pd
url = 'data/titanic.csv'
df = pd.read_csv(url)
df.head()
```

Fill in the missing values in the 'Age' column with the mean age of the passengers. The 'inplace=True' argument will make sure the changes are saved to the DataFrame.
```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

Create a new column 'Age_group' which categorizes passengers into 'Child(<13)', 'Teen(<20)', 'Adult(<60)', and 'Elderly(>=60)' based on their age. Display the new age groups to verify that they have been created correctly.
```python
def age_group(age):
    if age < 13: return 'Child'
    elif age < 20: return 'Teen'
    elif age < 60: return 'Adult'
    else: return 'Elderly'

df['Age_group'] = df['Age'].apply(age_group)
df['Age_group']
```

Visualize the distribution of 'Age_group' using a bar graph. This will help us understand the distribution in a more intuitive way.
```python
import matplotlib.pyplot as plt
df['Age_group'].value_counts().plot(kind='bar')
plt.title('Distribution of Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()
```


Calculate the survival rate per age group. This can be done by dividing the number of survivors in each age group by the total number of passengers in the age group. Display the survival rate of adults. Keep to 2 decimal places.
```python
survival_rate = df[df['Survived'] == 1].groupby('Age_group').size() / df.groupby('Age_group').size()
survival_rate['Adult'].round(2)

```

Finally, plot the survival rate per age group using a bar graph. This will help us visualize the survival rate among different age groups.
```python
survival_rate.plot(kind='bar')
plt.title('Survival Rate per Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.show()
```