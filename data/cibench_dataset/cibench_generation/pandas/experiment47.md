---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: airline-passengers Dataset
  difficulty: Easy
  module: pandas
  idx: 47
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules:
    - pandas
    - pandas&matplotlib
    - pandas&matplotlib
    - pandas&matplotlib
    - pandas&matplotlib
---


File Path: `data/airline-passengers.csv`

Load the AirPassengers.csv file from the provided path using the pandas read_csv function. This function returns a dataframe. Display the first 5 rows.
```python
import pandas as pd
df = pd.read_csv('data/airline-passengers.csv')
df.head()
```

The 'Month' column is currently of object type. Convert this to a datetime type using the pandas to_datetime() function. Set the 'Month' column as the index of the dataframe using the set_index() function. Visualize the 'Passengers' column over time by creating a line plot using matplotlib. The x-axis represents the month and the y-axis represents the number of passengers.
```python
df['Month'] = pd.to_datetime(df['Month'])
df = df.set_index('Month')
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df.index, df['Passengers'])
plt.title("Air Passengers Over Time")
plt.show()
```

Resample the dataframe by 'Quarter' using the resample() function and calculate the mean value of 'Passengers' in each quarter using the mean() function. Visualize the resampled 'Passengers' column over time by creating another line plot. The x-axis represents the quarter and the y-axis represents the number of passengers.
```python
quarter_df = df.resample('Q').mean()

plt.figure(figsize=(10,6))
plt.plot(quarter_df.index, quarter_df['Passengers'])
plt.title("Air Passengers Over Time (Quarterly)")
plt.show()
```

Calculate the rolling mean with a window size of 4 on the 'Passengers' column of the resampled dataframe using the rolling() and mean() functions. Visualize the rolling mean along with the original 'Passengers' data by creating a line plot. This helps to understand the trend in the data.
```python
quarter_df['rolling_mean'] = quarter_df['Passengers'].rolling(window=4).mean()

plt.figure(figsize=(10,6))
plt.plot(quarter_df.index, quarter_df['Passengers'], label='Original')
plt.plot(quarter_df.index, quarter_df['rolling_mean'], label='Rolling Mean')
plt.legend(loc='best')
plt.title("Rolling Mean of Air Passengers (Quarterly)")
plt.show()
```

Calculate the rolling standard deviation with a window size of 4 on the 'Passengers' column of the resampled dataframe. Visualize the rolling standard deviation along with the original 'Passengers' data by creating another line plot. This helps to understand the volatility in the data.
```python
quarter_df['rolling_std'] = quarter_df['Passengers'].rolling(window=4).std()
plt.figure(figsize=(10,6))
plt.plot(quarter_df.index, quarter_df['Passengers'], label='Original')
plt.plot(quarter_df.index, quarter_df['rolling_std'], label='Rolling Std')
plt.legend(loc='best')
plt.title("Rolling Standard Deviation of Air Passengers (Quarterly)")
plt.show()
```
