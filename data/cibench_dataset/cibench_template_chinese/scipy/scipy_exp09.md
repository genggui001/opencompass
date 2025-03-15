---
jupyter:
  title: 列处理和行聚类
  dataset: 匹兹堡树木数据集
  difficulty: 中级
  module: scipy
  idx: 9
  num_steps: 6
  step_types:
     - exec
     - num
     - num
     - num
     - num
     - exec
  modules:
     - pandas
     - scipy & numpy
     - scipy
     - scipy
     - scipy
     - scipy
---


文件路径：'data/scipy_dataset09.csv'.

### 从文件路径加载数据集并转换为 pandas 数据框。选择 'gbk' 作为编码模式。删除['height', 'width', 'growth_space_length', 'growth_space_width']列中包含非数值数据的行。获取前5行数据的信息。
```python
import pandas as pd
csv_filename = 'data/scipy_dataset09.csv'
data = pd.read_csv(csv_filename, header = 0, encoding='gbk')
columns_to_convert = ['height',	'width',	'growth_space_length',	'growth_space_width']
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')
data = data.dropna(subset=columns_to_convert)
data.head()
```

### 计算第7列的均值、中位数、方差、偏度和峰度。将所有结果相加并打印保留两位小数后的结果。
```python
import numpy as np
from scipy import stats
column_7 = data.iloc[:,6]
mean = column_7.mean()
median = column_7.median()
variance = column_7.var()
skewness = column_7.skew()
kurtosis = column_7.kurtosis()
value = sum([mean, median, variance, skewness, kurtosis])
round(value,2)
```

### 对第7列进行 Shapiro-Wilk 正态性检验。加和 Shapiro-Wilk 检验统计量和 p 值，打印保留两位小数后的结果。
```python
from scipy.stats import shapiro
statistic, p_value = stats.shapiro(column_7)
result = statistic + p_value
round(result,2)
```

### 使用 t 检验比较第7列和第8列之间的差异。加和 t 统计量和 p 值，打印保留两位小数后的结果。
```python
from scipy.stats import ttest_ind
column_8 = data.iloc[:, 7]
statistic, p_value = stats.ttest_ind(column_7, column_8)
result = statistic + value
round(result,2)
```

### 对第8列和第9列进行线性回归分析。将斜率、截距、r 值、p 值和标准误差相加并打印保留两位小数后的结果。
```python
from scipy.stats import linregress
column_8 = data.iloc[:, 7]
column_9 = data.iloc[:, 8]
result = linregress(column_8, column_9)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### 将第7、8、9和10列的所有行进行 K 均值聚类，得到4个簇。添加一个名为 "Cluster" 的列到数据框中，并用每行所属的类别填充该列。打印索引为15的数据的簇。
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data.iloc[:, [6,7,8,9]].astype(float)
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```

  