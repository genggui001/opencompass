---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: DS Salary 
  difficulty: Middle
  module: pandas
  idx: 9
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

File Path: `data/pandas_dataset09.csv`

Load the dataset from the file path into a pandas DataFrame. Display the column names.

```python
import pandas as pd
df = pd.read_csv("data/pandas_dataset09.csv")
df.columns
```

Calculate and display the number of all missing values in this dataset.

```python
sum(df.isnull().sum())
```

Replace missing values in work_year with the median value of the same column and then remove any remaining rows with missing values. Show the remaining total number of examples in this dataset.

```python
df['work_year'].fillna(df['work_year'].median(), inplace=True)
df.dropna(inplace=True)
len(df)
```

Give the data distribution of the square root of salary with red theme.

```python
import seaborn as sns
import numpy as np
sns.displot(np.sqrt(df['salary']), color='red')
```

How many samples have at least two outliers in salary, salary_in_usd and remote_ratio independently. Set outliner zscore greater than 2.

```python
from scipy.stats import zscore
from collections import defaultdict

def get_indices(df, column):
    z_scores = zscore(df[column])
    abs_z_scores = np.abs(z_scores)
    return np.where(abs_z_scores > 2)[0]

column_names = ['salary', 'salary_in_usd', 'remote_ratio']

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

Group and aggregate data by work_year and calculate the average of each numerical column. Find out how many attributes have a strict positive correlation with work_year.

```python
# Select only the numeric columns as df_num
df_num = df.select_dtypes(include=['float64', 'int64'])
grouped_df = df_num.groupby('work_year').agg(['mean'])
count = 0
for col in grouped_df.columns:
    count += (grouped_df[col].diff().dropna() > 0).all()
count
```