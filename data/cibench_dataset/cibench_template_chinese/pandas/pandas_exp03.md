---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Iris dataset
  difficulty: Easy
  module: pandas
  idx: 3
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
文件路径： `data/pandas_dataset03.csv`

加载数据集到pandas DataFrame中。显示列名。

```python
import pandas as pd
df = pd.read_csv("data/pandas_dataset03.csv")
df.columns
```

计算并显示数据集中所有缺失值的数量。

```python
sum(df.isnull().sum())
```

将SepalLengthCm中的缺失值替换为相同列的中值，然后删除任何剩余的缺失值行。显示此数据集中剩余的总样本数。

```python
df['SepalLengthCm'].fillna(df['SepalLengthCm'].median(), inplace=True)
df.dropna(inplace=True)
len(df)
```

绘出平方根转换后SepalWidthCm列的数据分布，用红色主题。

```python
import seaborn as sns
import numpy as np
sns.displot(np.sqrt(df['SepalWidthCm']), color='red')
```

有多少样本至少有两个异常值在SepalWidthCm; PetalLengthCm; PetalWidthCm中。设置异常值zscore大于1。

```python
from scipy.stats import zscore
from collections import defaultdict

def get_indices(df, column):
    z_scores = zscore(df[column])
    abs_z_scores = np.abs(z_scores)
    return np.where(abs_z_scores > 1)[0]

column_names = ['SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

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

选择所有的 Iris-setosa 样本。并按PetalWidthCm对数据进行分组和聚合，并计算每个数值组的平均值。找出有多少属性与PetalWidthCm严格负相关。

```python
# Select only the numeric columns as df_num
df = df[df['Species'] == 'Iris-setosa']
df_num = df.select_dtypes(include=['float64', 'int64'])

grouped_df = df_num.groupby('PetalWidthCm').agg(['mean'])
count = 0
for col in grouped_df.columns:
    count += (grouped_df[col].diff().dropna() < 0).all()
count
```