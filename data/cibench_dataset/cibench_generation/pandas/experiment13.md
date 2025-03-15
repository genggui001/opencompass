---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: minimum temperatures Dataset
  difficulty: Easy
  module: pandas
  idx: 13
  num_steps: 4
  step_types:
    - exec
    - exec
    - vis
    - vis
  modules:
    - pandas
    - pandas
    - pandas&matplotlib
    - pandas&matplotlib
---

File Path: `data/daily-min-temperatures.csv`


Load the dataset from the provided path, which is in CSV format.
```python
import pandas as pd
url = 'data/daily-min-temperatures.csv'
df = pd.read_csv(url)
df.head()
```

Convert the 'Date' column in the DataFrame to a DateTime data type to facilitate time series analysis. Set the 'Date' column as the index of the DataFrame with inplacement.
```python
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
```


Resample the DataFrame to a monthly frequency. Plot the original daily temperature data and the resampled monthly data on the same graph.
```python
import matplotlib.pyplot as plt
monthly_df = df.resample('M').mean()
plt.plot(df, label='Daily')
plt.plot(monthly_df, label='Monthly')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Daily and Monthly Temperatures')
plt.legend()
plt.show()
```

Calculate a moving average of the 'Temp' column with a window size of 3. Plot the original temperature data and the calculated moving average on the same graph for comparison.
```python
df['Temp'].rolling(window=3).mean()
plt.plot(df['Temp'], label='Original')
plt.plot(df['Temp'].rolling(window=3).mean(), label='Moving Average')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature and Moving Average')
plt.legend()
plt.show()
```
