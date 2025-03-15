---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 35
  num_steps: 5
  step_types:
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
---

Create an interval index with a starting point of 0, an ending point of 5 and a frequency or step-size of 1. This will create an interval index from 0 to 5 with each interval being of size 1. Access the first element of the interval index.
```python
import pandas as pd 

int_index = pd.interval_range(start=0, end=5, freq=1)
int_index[0]
```

Display the length of each interval.
```python
int_index.length
```

Display the midpoint of each interval.
```python
int_index.mid
```

Check whether the first interval overlaps with the third interval.
```python
int_index[0].overlaps(int_index[2])
```

Compute the intersection of the interval index with a new interval index that starts at 2 and ends at 6 with a frequency of 1.
```python
int_index.intersection(pd.interval_range(start=2, end=6, freq=1))
```