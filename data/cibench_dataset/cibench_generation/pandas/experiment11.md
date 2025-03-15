---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Iris Dataset
  difficulty: Easy
  module: pandas
  idx: 11
  num_steps: 6
  step_types:
    - exec
    - exec
    - text
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

File Path: `data/iris.csv`

Load the Iris dataset from path.

```python
import pandas as pd
df = pd.read_csv('data/iris.csv')
```

Group the dataframe by 'species' column and calculate the mean of other columns for each species.

```python
grouped_df = df.groupby('species').mean()
```

Transpose the grouped dataframe. Reset the index of the transposed dataframe. Rename the 'index' column of the dataframe to 'measurement'. Display the columns of the transposed dataframe.

```python
transposed_df = grouped_df.T
transposed_df = transposed_df.reset_index()
transposed_df = transposed_df.rename(columns={'index':'measurement'})
transposed_df.columns
```

Reshape the dataframe to a long format with 'measurement' as the identifier variable, 'species' as the variable column and 'mean' as the value column. Display the mean for 'setosa' species of all measurement. Keep to two decimal places by rounding the values.
```python
melted_df = transposed_df.melt('measurement', var_name='species', value_name='mean')
melted_df[melted_df['species'] == 'setosa']['mean'].mean().round(2)
```

Reshape the melted dataframe back to a wide format with 'measurement' as the index, 'species' as the columns, and 'mean' as the values. Display the petal length mean of setosa species. Keep to two decimal places by rounding the values.
```python
pivoted_df = melted_df.pivot(index='measurement', columns='species', values='mean')
pivoted_df['setosa']['petal_length'].round(2)
```

Visualize the previous dataframe using a bar chart. Add a title to the chart and labels for x and y axis respectively.
```python
import matplotlib.pyplot as plt 

pivoted_df.plot(kind='bar')
plt.title('Mean Measurements of Iris Species')
plt.xlabel('Measurement')
plt.ylabel('Mean')
plt.show()
```
