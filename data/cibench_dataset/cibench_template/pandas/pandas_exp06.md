---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Education
  difficulty: Middle
  module: pandas
  idx: 6
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

File Path: `data/pandas_dataset06.xlsx`

Load the dataset from the file path into a pandas DataFrame. Display the column names.

```python
import pandas as pd
df = pd.read_excel("data/pandas_dataset06.xlsx")
df.columns
```

Calculate and display the number of all missing values in this dataset.

```python
sum(df.isnull().sum())
```

Replace missing values in Exam Score with the median value of the same column and then remove any remaining rows with missing values. Show the remaining total number of examples in this dataset.

```python
df['Exam Score'].fillna(df['Exam Score'].median(), inplace=True)
df.dropna(inplace=True)
len(df)
```

Give the data distribution of the square root of Attendance with red theme.

```python
import seaborn as sns
import numpy as np
sns.displot(np.sqrt(df['Attendance']), color='red')
```

How many samples have at least two outliers in Attendance, homework completion and online exam count independently. Set outliner zscore greater than 1.

```python
from scipy.stats import zscore
from collections import defaultdict

def get_indices(df, column):
    z_scores = zscore(df[column])
    abs_z_scores = np.abs(z_scores)
    return np.where(abs_z_scores > 1)[0]

column_names = ['Attendance', 'Homework Completion', 'Online Exam Count']

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

Mapping performance, 0 for average, 1 for good, 2 for excellent, then group and aggregate data by performance and calculate the average of each column. Find out how many attributes have a strict positive correlation with performance.

```python
# Select only the numeric columns as df_num
df['Performance'] = df['Performance'].map(
  {'average': 0, 'good': 1, 'excellent': 2}
)
grouped_df = df.groupby('Performance').agg(['mean'])
count = 0
for col in grouped_df.columns:
    count += (grouped_df[col].diff().dropna() > 0).all()
count
```