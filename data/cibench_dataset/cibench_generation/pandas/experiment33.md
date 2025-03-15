---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 33
  num_steps: 6
  step_types:
    - exec
    - exec
    - text
    - exec
    - exec
    - exec
  modules:
    - pandas&numpy
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---


Construct a pandas DataFrame from a dictionary. The dictionary has keys 'A' to 'E', with values of different data types including a float, timestamp, series, NumPy array, and categorical data.
```python
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"])})
df
```


Create another DataFrame with an additional column 'F' with string values. This demonstrates how to add more data to an existing DataFrame.
```python
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
df2
```


Print the index of the first DataFrame.
df.index
```

Transpose the DataFrame.
```python
df.T
```

Sort the DataFrame by an axis.
```python
df.sort_index(axis=1, ascending=False)
```

Sort the DataFrame by values in a specific column.
```python
df.sort_values(by='B')
```
