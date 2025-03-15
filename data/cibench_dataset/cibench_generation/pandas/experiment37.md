---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: earthquake-database
  difficulty: Easy
  module: pandas
  idx: 37
  num_steps: 7
  step_types:
    - exec
    - exec
    - num
    - vis
    - exec
    - num
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
    - pandas
    - pandas
    - pandas&matplotlib
---

File Path: `data/earthquakes-23k.csv`

Load the earthquake data into a pandas dataframe from the CSV file.

```python
import pandas as pd
df = pd.read_csv('data/earthquakes-23k.csv')
df.head()
```

Convert the 'Date' column of the dataframe from a string to a Datetime format. Now, extract the year from the 'Date' column and store it in a new column, 'year'.
```python
df['Date'] = pd.to_datetime(df['Date'],errors='coerce', utc=True)
df['year'] = df['Date'].dt.year
```

Count the number of earthquakes for each year and sort the counts in ascending order of years. Display the count of earthquakes of 2016.
```python
earthquakes_per_year = df['year'].value_counts().sort_index()
earthquakes_per_year[2016]
```

Plot the number of earthquakes per year. The x-axis represents the year and the y-axis represents the number of earthquakes.
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(earthquakes_per_year.index, earthquakes_per_year.values)
plt.title('Number of Earthquakes Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Earthquakes')
plt.grid()
plt.show()
```

Similarly, extract the month from the 'Date' column and store it in a new column, 'month'.
```python
df['month'] = df['Date'].dt.month
```


Count the number of earthquakes for each month and sort the counts in ascending order of months. Display the count of earthquakes of month 1.
```python
earthquakes_per_month = df['month'].value_counts().sort_index()
earthquakes_per_month[1]
```

Plot the number of earthquakes per month. The x-axis represents the month and the y-axis represents the number of earthquakes.
```python
plt.figure(figsize=(12,6))
plt.plot(earthquakes_per_month.index, earthquakes_per_month.values)
plt.title('Number of Earthquakes Per Month')
plt.xlabel('Month')
plt.ylabel('Number of Earthquakes')
plt.grid()
plt.show()
```
