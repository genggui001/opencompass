---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Tip Dataset
  difficulty: Easy
  module: pandas
  idx: 6
  num_steps: 4
  step_types:
    - exec
    - num
    - text
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
---

File Path: `data/tips.csv`

Load the dataset from the given path into a pandas DataFrame. Display the first five rows of the dataset to verify the data has been loaded correctly.

```python
import pandas as pd

data = pd.read_csv('data/tips.csv')
data.head()
```

Check for and display the sum of number of missing values in each column of the dataset.
```python
data.isnull().sum().sum()
```

Display Data Types of each column in the dataset. Convert all the none-numeric columns to numeric type.
```python
data.dtypes
```

Plot a histogram of the total bill to visualize its distribution using Matplotlib. Set the number of bins to 10, and the color to 'skyblue'. Also, set the title of the plot to 'Total Bill Distribution', and label the x-axis as 'Total Bill'.
```python
import matplotlib.pyplot as plt

data['total_bill'].plot.hist(bins=10, color='skyblue')
plt.title('Total Bill Distribution')
plt.xlabel('Total Bill')
plt.show()
```
