---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Titanic Dataset
  difficulty: Easy
  module: pandas
  idx: 14
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
    - pandas&numpy
    - pandas&numpy
    - pandas&&matplotlib
---

File Path: `data/titanic.csv`


Load the Titanic dataset from the path into a pandas DataFrame.
```python
import pandas as pd 
url = 'data/titanic.csv'
df = pd.read_csv(url)
df.head()
```

Create a new column 'Age_times_class' which is the product of 'Age' and 'Pclass' (Passenger Class).
```python
df['Age_times_class'] = df.apply(lambda row: row.Age * row.Pclass, axis=1)
```

Divide 'Fare' into 4 intervals and count the number of passengers in each interval. Display the number of passengers in the most expensive interval.
```python
fare_intervals = pd.cut(df['Fare'], bins=4)
fare_intervals.value_counts().iloc[-1]
```

Calculate the mean age of passengers for each 'Sex' and 'Pclass'. Display the mean of Pclass = 1 & sex = male. Keep to 2 decimal places.
```python
import numpy as np
pivot_table = df.pivot_table(values='Age', index='Sex', columns='Pclass', aggfunc=np.mean)
round(pivot_table.loc["male", 1], 2)
```

Apply a function to every cell of a new DataFrame containing 'Age' and 'Fare' columns. The function will be np.ceil which rounds up each value to the nearest integer. Display the first age value in the new DataFrame.
```python
df_subset = df[['Age', 'Fare']]
df_subset = df_subset.applymap(np.ceil)
df_subset['Age'][0]
```

Plot the previously created pivot table to visualize the average age by sex and passenger class.
```python
import matplotlib.pyplot as plt
pivot_table.plot(kind='bar')
plt.ylabel('Average Age')
plt.title('Average Age by Sex and Passenger Class')
plt.show()
```