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

文件路径： `data/pandas_dataset04.xlsx`

加载数据集到pandas DataFrame中。显示列名。

```python
import pandas as pd
df = pd.read_excel("data/pandas_dataset04.xlsx")
df.columns
```

计算并显示数据集中所有缺失值的数量。

```python
sum(df.isnull().sum())
```

将weight中的缺失值替换为相同列的中值，然后删除任何剩余的缺失值行。显示此数据集中剩余的总样本数。

```python
df['Weight'].fillna(df['Weight'].median(), inplace=True)
df.dropna(inplace=True)
len(df)
```

绘出平方根转换后height列的数据分布，用红色主题。

```python
import seaborn as sns
import numpy as np
sns.displot(np.sqrt(df['Height']), color='red')
```

有多少样本至少有两个异常值在blood sugar; oxygen saturation; white blood cell count中。设置异常值zscore大于2。

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

按health status分组并聚合数据，计算每个组的平均值。找出有多少属性与健康程度严格负相关。（越健康，值越低）

```python
grouped_df = df.groupby('Health Status').agg(['mean'])
count = 0
for col in grouped_df.columns:
    count += (grouped_df[col].diff().dropna() > 0).all()
count
```