---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Auto MPG dataset
  difficulty: Easy
  module: pandas
  idx: 49
  num_steps: 7
  step_types:
    - exec
    - text
    - text
    - text
    - text
    - vis
    - text
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
    - pandas
---

File Path: `data/auto-mpg.csv`

Load the Auto MPG dataset from the path.
```python
import pandas as pd
url = 'data/auto-mpg.csv'
df = pd.read_csv(url)
df.head()
```

Break down the 'Car Name' column into single words. Then, count the occurrences of each word. Display the five most common words.
```python
df['Car Name'].str.split(' ').explode().value_counts().head()
```

Divide the 'MPG' column into five bins labeled as 'Very Low', 'Low', 'Medium', 'High', and 'Very High', then count the number of values in each bin.
```python
pd.cut(df['MPG'], bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High']).value_counts()
```

Group the DataFrame by the 'Cylinders' column again. This time, calculate both the minimum and maximum 'MPG' for each group. Name the output columns as 'min_mpg' and 'max_mpg'.
```python
df.groupby('Cylinders')['MPG'].agg(min_mpg='min', max_mpg='max')
```

Merge the 'Car Name' and 'MPG' columns with the 'Car Name' and 'Cylinders' columns based on 'Car Name'. This process will combine the two sets of columns into one DataFrame, with an indicator column showing the source of each row and suffixes added to the overlapping column names.
```python
df1 = df[['Car Name', 'MPG']]
df2 = df[['Car Name', 'Cylinders']]
merged_df = df1.merge(df2, on='Car Name', how='inner', indicator=True, suffixes=('_df1', '_df2'))
merged_df['_merge'].value_counts()
```

Plot the 'MPG' and 'Cylinders' columns in separate subplots, arranged in two rows and one column. This visualization will provide a graphical representation of the data in these two columns.
```python
import matplotlib.pyplot as plt
df[['MPG', 'Cylinders']].plot(subplots=True, layout=(2,1))
plt.tight_layout()
plt.show()
```

Create a pivot table for the 'MPG' values, indexed by 'Cylinders' and columned by 'Model Year'. Include margins for subtotals and grand totals, named as 'Total'.
```python
df.pivot_table('MPG', index='Cylinders', columns='Model Year', margins=True, margins_name='Total')
```