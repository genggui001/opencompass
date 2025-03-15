---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Wine Quality Dataset
  difficulty: Easy
  module: pandas
  idx: 23
  num_steps: 6
  step_types:
    - exec
    - text
    - text
    - text
    - text
    - text
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---


File Path: `data/winequality-red.csv`


Load the Wine Quality dataset.
```python
import pandas as pd
df = pd.read_csv("data/winequality-red.csv")
df.head()
```

Calculate the median of all numerical columns.
```python
df.median()
```

Compute the standard deviation of all numerical columns.
```python
df.std()
```

Calculate the variance of all numerical columns.
```python
df.var()
```

Calculate the skewness of each numerical column.
```python
df.skew()
```

Calculate the kurtosis of each numerical column.
```python
df.kurtosis()
```