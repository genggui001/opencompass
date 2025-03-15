---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 28
  num_steps: 6
  step_types:
    - exec
    - exec
    - text
    - num
    - text
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - seaborn&numpy
    - scipy
    - pandas
---


Add and subtract 5 days to/from the date '2022-01-01'. Display of the timestamps.
```python
import pandas as pd
print(pd.Timestamp('2022-01-01') + pd.Timedelta(days=5))
print(pd.Timestamp('2022-01-01') - pd.Timedelta(days=5))
```

We will convert a list of strings ('1 days', '1 days 00:00:05', '2 days 00:00:05', '3 days') that represent time durations to Timedelta objects.
```python
pd.to_timedelta(['1 days', '1 days 00:00:05', '2 days 00:00:05', '3 days'])
```

We will convert the difference between a series of dates(starting from 2022-01-01 with 5 periods of days) and '2022-01-01' to day units.
```python
(pd.Series(pd.date_range('2022-01-01', periods=5, freq='D')) - pd.Timestamp('2022-01-01')).dt.days
```

We will create a timedelta object representing '31 days 5 min 3 sec', and then access the number of days in it.
```python
td = pd.Timedelta('31 days 5 min 3 sec')
td.days
```

We will create a dataframe with dates from '2022-01-01' to '2022-12-31' and calculate the difference from '2022-06-01'. Display the dataframe.
```python
df = pd.DataFrame({'time': pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')})
df['timedelta'] = df['time'] - pd.Timestamp('2022-06-01')
df
```

We will plot the difference in days from '2022-06-01' for each date in the dataframe created in the previous step.
```python
import matplotlib.pyplot as plt
df['timedelta'].dt.days.plot()
plt.show()
```
