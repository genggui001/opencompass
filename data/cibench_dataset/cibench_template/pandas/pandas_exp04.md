---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Medical
  difficulty: Middle
  module: pandas
  idx: 4
  num_steps: 6
  step_types:
    - exec
    - num
    - num
    - vis
    - num
    - num
  modules:
    - pandas
    - pandas
    - pandas
    - seaborn&numpy
    - scipy
    - pandas
---

File Path: `data/pandas_dataset04.xlsx`

Load the dataset from the file path into a pandas DataFrame. Display the column names.

```python
import pandas as pd
df = pd.read_excel("data/pandas_dataset04.xlsx")
df.columns
```

Calculate and display the number of all missing values in this dataset.

```python
sum(df.isnull().sum())
```

Replace missing values in weight with the median value of the same column and then remove any remaining rows with missing values. Show the remaining total number of examples in this dataset.

```python
df['Weight'].fillna(df['Weight'].median(), inplace=True)
df.dropna(inplace=True)
len(df)
```

Give the data distribution of the square root of height with red theme.

```python
import seaborn as sns
import numpy as np
sns.displot(np.sqrt(df['Height']), color='red')
```

How many samples have at least two outliers in blood sugar, oxygen saturation and white blood cell count independently. Set outliner zscore greater than 2.

```python
from scipy.stats import zscore
from collections import defaultdict

def get_indices(df, column):
    z_scores = zscore(df[column])
    abs_z_scores = np.abs(z_scores)
    return np.where(abs_z_scores > 2)[0]

column_names = ['Blood Sugar', 'Oxygen Saturation', 'White Blood Cell Count']

# 创建一个字典来计算每个元素出现的次数
counts = defaultdict(int)
for column in column_names:
    indices = get_indices(df, column)
    for item in indices:
        counts[item] += 1

# 找出出现两次及以上的元素
duplicates = {item for item, count in counts.items() if count >= 2}
len(duplicates)
```

Group and aggregate data by health status and calculate the average of each columns. Find out how many attributes have a strict negative correlation with weight.(Healthier, lower values)

```python
grouped_df = df.groupby('Health Status').agg(['mean'])
count = 0
for col in grouped_df.columns:
    count += (grouped_df[col].diff().dropna() > 0).all()
count
```