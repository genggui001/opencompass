---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: None
  difficulty: Easy
  module: pandas
  idx: 3
  num_steps: 6
  step_types:
    - num
    - num
    - num
    - text
    - num
    - num
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
---

Create a list of numbers from 1 to 5 and convert it into a pandas series. Display the first elements of the series.
```python
import pandas as pd
numbers = [1, 2, 3, 4, 5]
series = pd.Series(numbers)
series[0]
```

Create a dictionary where keys are 'a', 'b', 'c', 'd', 'e' and values are 1, 2, 3, 4, 5 respectively. Convert this dictionary into a pandas series. Display the value of the element associated with the key 'c'.
```python
data = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
series = pd.Series(data)
series['c']
```

Create a series of numbers from 1 to 5 and assign custom indexes 'A', 'B', 'C', 'D', 'E' to them. Display the value of the element associated with the index 'C'.
```python
series = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
series['C']
```

Slice the series to get the elements from the second to the fourth position, which are associated with indexes 'B' to 'D'.
```python
series['B':'D']
```

Apply the natural logarithm function to each element in the series. Display the second elements of the series. Keep to two decimal places.
```python
import numpy as np
series = series.apply(np.log)
series[1].round(2)
```

Filter the new series to get elements that are greater than 0.3. Display the number of elements in the filtered series.
```python
filtered_series = series[series > 0.3]
len(filtered_series)
```

