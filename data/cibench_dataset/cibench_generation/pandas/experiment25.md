---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 25
  num_steps: 5
  step_types:
    - exec
    - vis
    - text
    - vis
    - exec
  modules:
    - pandas&numpy
    - pandas&matplotlib
    - pandas
    - seaborn&matplotlib
    - pandas
---


Create a date range starting from 1st January 2022 for a period of 15 days. This will serve as the index for our DataFrame. Using the date range created above as the index, create a DataFrame with 15 rows and 5 columns. Fill the DataFrame with random numbers.
```python
import pandas as pd
import numpy as np
dates = pd.date_range('1/1/2022', periods=15)
df = pd.DataFrame(np.random.randn(15, 5), index=dates, columns=list('ABCDE'))
```

Add a new column to the DataFrame named 'Time_Delta'. The values of this column should be the difference in days between the date in the index and 1st January 2022. Plot a line graph of 'Time_Delta' over time to visually understand the trend. 
```python
import matplotlib.pyplot as plt
df['Time_Delta'] = (df.index - pd.Timestamp('2022-01-01')).days
df['Time_Delta'].plot(kind='line', title='Time Delta over Time')
plt.show()
```

Count the number of unique days in 'Time_Delta' and calculate the frequency of each day.
```python
df['Time_Delta'].nunique()
df['Time_Delta'].value_counts()
```


Calculate the cumulative sum of 'Time_Delta' and add it as a new column to the DataFrame. Plot a line graph of 'Cumulative_Sum' over time.
```python
df['Cumulative_Sum'] = df['Time_Delta'].cumsum()
df['Cumulative_Sum'].plot(kind='line', title='Cumulative Sum of Time Delta over Time')
plt.show()
```


Calculate the correlation between 'Time_Delta' and 'Cumulative_Sum' to understand the relationship between these variables.
```python
df[['Time_Delta', 'Cumulative_Sum']].corr()
```
