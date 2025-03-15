---
jupyter:
  title: 列处理和行聚类
  dataset: 印第安人糖尿病数据集
  difficulty: 中级
  module: scipy
  idx: 2
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

文件路径：'data/scipy_dataset02.csv'.

### 从文件路径加载数据集并转换为 pandas 数据框。获取前5行数据的信息。
```python
import pandas as pd
csv_filename = 'data/scipy_dataset02.csv'
data = pd.read_csv(csv_filename, header = None)
data.head()
```

### 计算第4列的均值、中位数、方差、偏度和峰度。将所有结果相加并打印保留两位小数后的结果。
```python
import numpy as np
from scipy import stats
column_4 = data.iloc[:, 3]
mean = column_4.mean()
median = column_4.median()
variance = column_4.var()
skewness = column_4.skew()
kurtosis = column_4.kurtosis()
value = sum([mean, median, variance, skewness, kurtosis])
round(value,2)
```

### 对第5列进行Shapiro-Wilk正态性检验。将Shapiro-Wilk检验统计量和p值加和，打印保留两位小数后的结果。
```python
from scipy.stats import shapiro
column_5 = data.iloc[:, 4]
statistic, p_value = stats.shapiro(column_5)
result = statistic + p_value
round(result,2)
```

### 使用 t 检验比较第2列和第3列之间的差异。将 t 统计量和 p 值加和，打印保留两位小数后的结果。
```python
from scipy.stats import ttest_ind
column_2 = data.iloc[:, 1]
column_3 = data.iloc[:, 2]
statistic, p_value = stats.ttest_ind(column_2, column_3)
result = statistic + value
round(result,2)
```

### 对第6列和第7列进行线性回归分析。将斜率、截距、r值、p值和标准误差相加并打印保留两位小数后的结果。
```python
from scipy.stats import linregress
column_6 = data.iloc[:, 5]
column_7 = data.iloc[:, 6]
result = linregress(column_6, column_7)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### 将所有列的所有行进行K均值聚类，得到4个簇。添加一个名为 "Cluster" 的列到数据框中，并用每行所属的类别填充该列。打印索引为15的数据的簇。
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data[[1,2,3,4,5,6,7,8]]
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```
   