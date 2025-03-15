---
jupyter:
  title: Analysis of Air Quality Dataset
  module: seaborn
  dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/00360/AirQualityUCI.csv
  difficulty: HARD
  idx: 36
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - pandas
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---

File Path: 'data/AirQualityUCI.csv'. 

Load the dataset from the provided URL using pandas read_csv function. Use sep as ';' and decomal ','. Make sure to parse 'Date' and 'Time' columns as datetime data type. Rename the 'Date_Time' column to 'DateTime'. Drop the final two empty columns. Only get first 500 rows.
```python
import pandas as pd
df = pd.read_csv('data/AirQualityUCI.csv', sep=';', decimal=',', parse_dates=[['Date', 'Time']])
df.rename(columns={"Date_Time": "DateTime"}, inplace=True)
df = df.iloc[:500, :-2]
```

Plot a lineplot for "CO(GT)" values against time.
```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x="DateTime", y="CO(GT)", data=df)
plt.show()
df = df[df['CO(GT)'] != -200.0]
```

The dataset has some rows where 'CO(GT)' is -200.0, which seems to be an error or missing value. Filter out these rows from the dataframe. Plot a lineplot for "CO(GT)" values against time after filtering out erroneous rows.
```python
df = df[df['CO(GT)'] != -200.0]
sns.lineplot(x="DateTime", y="CO(GT)", data=df)
plt.show()
```

Set 'DateTime' as the index of the dataframe inplace use correct format. Resample the dataframe to daily frequency and calculate the mean of each day's data. Plot a lineplot for daily average "CO(GT)" values against time.
```python
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d/%m/%Y %H.%M.%S', errors='coerce')
df.set_index('DateTime', inplace=True)
df_daily = df.resample('D').mean()
sns.lineplot(data=df_daily['CO(GT)'])
plt.show()
```

Resample the dataframe to hourly frequency and calculate the mean of each hour's data. Plot a lineplot for hourly average "CO(GT)" values against time.
```python
df_hourly = df.resample('H').mean()
sns.lineplot(data=df_hourly['CO(GT)'])
plt.show()
```
