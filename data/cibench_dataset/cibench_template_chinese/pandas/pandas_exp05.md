---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Financial
  difficulty: Middle
  module: pandas
  idx: 5
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

文件路径： `data/pandas_dataset05.xlsx`

加载数据集到pandas DataFrame中。显示列名。

```python
import pandas as pd
df = pd.read_excel("data/pandas_dataset05.xlsx")
df.columns
```

计算并显示数据集中所有缺失值的数量。

```python
sum(df.isnull().sum())
```

将Monthly Income中的缺失值替换为相同列的中值，然后删除任何剩余的缺失值行。显示此数据集中剩余的总样本数。

```python
df['Monthly Income'].fillna(df['Monthly Income'].median(), inplace=True)
df.dropna(inplace=True)
len(df)
```

绘出平方根转换后Balance列的数据分布，用红色主题。

```python
import seaborn as sns
import numpy as np
sns.displot(np.sqrt(df['Balance']), color='red')
```

有多少样本至少有两个异常值在balance; debt; age中。设置异常值zscore大于1.5。

```python
from scipy.stats import zscore
from collections import defaultdict

def get_indices(df, column):
    z_scores = zscore(df[column])
    abs_z_scores = np.abs(z_scores)
    return np.where(abs_z_scores > 1.5)[0]

column_names = ['Balance', 'Debt', 'Age']

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

去掉与日期相关的列，按信用等级分组并聚合数据，并计算每个数字组的平均值。找出有多少属性与信用等级严格正相关。（C等级是最高的信用等级）

```python
df = df.drop('Last Loan Date', axis=1)
grouped_df = df.groupby('Credit Rating').agg(['mean'])
count = 0
for col in grouped_df.columns:
    count += (grouped_df[col].diff().dropna() > 0).all()
count
```