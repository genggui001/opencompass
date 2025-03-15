---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Countries dataset
  difficulty: Easy
  module: pandas
  idx: 4
  num_steps: 5
  step_types:
    - exec
    - text
    - text
    - num
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
---

File Path: `data/countries.csv`

Load a DataFrame from a CSV file located at the provided URL.
```python
import pandas as pd 

df = pd.read_csv('data/countries.csv')
df.head()
```

Access both the country and region columns in the data.
```python
df[['Country', 'Region']]
```

Access the country value in the first row of the data. 
```python
df.loc[0, 'Country']
```

Filter the DataFrame 'df' to only include rows of south america. Display the number of rows in the filtered DataFrame.
```python
len(df[df['Region'] == 'SOUTH AMERICA'])
```

Plot the count of each region in the DataFrame 'df' with a bar plot. 
```python
import matplotlib.pyplot as plt

df['Region'].value_counts().plot(kind='bar')
plt.show()
```