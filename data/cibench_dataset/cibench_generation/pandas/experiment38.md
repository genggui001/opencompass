---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 38
  num_steps: 4
  step_types:
    - exec
    - exec
    - exec
    - text
  modules:
    - pandas&numpy
    - pandas
    - pandas
    - pandas
---

Generate an array of floating point numbers ranging from 0 to 1, in increments of 0.1. This array will serve as the index for our DataFrame. We will use the `Float64Index` function from pandas and the `arange` function from numpy. Create a DataFrame that consists of a single column filled with 10 random numbers.
```python
import pandas as pd
import numpy as np
index = pd.Float64Index(np.arange(0, 1, 0.1))
df = pd.DataFrame(np.random.randn(10), index=index)
```

Access the row in the DataFrame that is associated with the index value of 0.2 by.
Update the value in the DataFrame row associated with the index value of 0.5 to 0.
Remove the row in the DataFrame that is associated with the index value of 0.4.
```python
df.loc[0.2]
df.loc[0.5] = 0
df = df.drop(0.4)
```

Reset the DataFrame's index to the default integer index. The updated DataFrame should be saved back to the variable `df`.
```python
df = df.reset_index()
```

Check the type of the DataFrame's index again. This will confirm that our DataFrame now uses the default integer index.
```python
type(df.index)
```