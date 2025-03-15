---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 40
  num_steps: 7
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
    - exec
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
---


Create a pandas DataFrame with random numbers. The DataFrame should be a 4x4 grid, with each cell filled by a random number. These random numbers can be generated using the numpy's random.randn function. The columns should be labeled as 'A', 'B', 'C', and 'D'.
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4,4), columns=list('ABCD'))
df
```

Create a new DataFrame with a MultiIndex. The MultiIndex should have three levels of indices named 'level_1', 'level_2', and 'level_3'. The DataFrame should be filled with random numbers and should have 125 rows and 2 columns.
```python
index = pd.MultiIndex.from_tuples([(i,j,k) for i in range(5) for j in range(5) for k in range(5)], names=['level_1', 'level_2', 'level_3'])
df2 = pd.DataFrame(np.random.rand(125, 2), index=index)
df2
```

Select all rows from the DataFrame where 'level_1' index is 1.
```python
df2.loc[1]
```

Retrieve data at 'level_2' index 1 from the DataFrame.
```python
df2.xs(1, level='level_2', axis=0)
```

Swap 'level_1' and 'level_2' indices in the DataFrame using the swaplevel function.
```python
df2 = df2.swaplevel('level_1', 'level_2')
df2
```

Calculate the mean of the DataFrame, grouped by 'level_2' index.
```python
mean_df = df2.groupby(level='level_2').mean()
mean_df
```

Finally, create a bar plot to visualize the mean of the DataFrame, grouped by 'level_2' index. Display the plot using plt.show().
```python
import matplotlib.pyplot as plt
mean_df.plot(kind='bar')
plt.show()
```