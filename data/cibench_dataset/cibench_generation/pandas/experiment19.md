---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: tips Dataset
  difficulty: Easy
  module: pandas
  idx: 19
  num_steps: 6
  step_types:
    - exec
    - num
    - num
    - num
    - num
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
---

File Path: `data/tips.csv`

Load the dataset from the provided path using the pandas read_csv() function. Assign this data to a variable called df.
```python
import pandas as pd
url = "data/tips.csv"
df = pd.read_csv(url)
```

Calculate the memory usage of the data frame df in MB. Convert it to MB by dividing by 1024 twice, and print the result. Keep to 4 decimal places.
```python
import sys
round(sys.getsizeof(df) / 1024 / 1024, 4)
```

Calculate the mean of the 'total_bill' column in df. Display it and keep to 2 decimal places.
```python
round(df['total_bill'].mean(), 2)
```

Create a new column 'tip_percentage' in df. The 'tip_percentage' is calculated as the percentage of 'tip' in 'total_bill'. Get index 2 tip_percentage value and keep to 2 decimal places.
```python
df['tip_percentage'] = df.apply(lambda row: row['tip'] / row['total_bill'] * 100, axis=1)
round(df['tip_percentage'][2], 2)
```


Change the data type of 'tip_percentage' column to 'float32' using the astype() method. Then, calculate and print the memory usage of df in MB. Keep to 4 decimal places.
```python
df['tip_percentage'] = df['tip_percentage'].astype('float32')
round(sys.getsizeof(df) / 1024 / 1024, 4)
```


Create a bar plot to visualize the memory usage at different stages: the original data frame, after adding the 'tip_percentage' column, and after dropping the 'tip_percentage' column. Use the sys.getsizeof() function to calculate memory usage. 
```python
import matplotlib.pyplot as plt
memory_usage = [sys.getsizeof(df), sys.getsizeof(df['tip_percentage']), sys.getsizeof(df.drop('tip_percentage', axis=1))]
labels = ['Original', 'After adding column', 'After dropping column']
plt.bar(labels, memory_usage)
plt.ylabel('Memory Usage (bytes)')
plt.show()
```
