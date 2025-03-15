---
jupyter:
  title: 列处理和行聚类
  dataset: 车祸数据集
  difficulty: 中级
  module: scipy
  idx: 3
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


文件路径：'data/scipy_dataset03.csv'.

### 从文件路径加载数据集并转换为 pandas 数据框。删除['MUNICIPALITY','POLICE_AGCY','TIME_OF_DAY','HOUR_OF_DAY']列中包含非数值数据的行。获取前5行数据的信息。
```python
import pandas as pd
csv_filename = 'data/scipy_dataset03.csv'
data = pd.read_csv(csv_filename, header = 0)
columns_to_convert = ['MUNICIPALITY','POLICE_AGCY','TIME_OF_DAY','HOUR_OF_DAY']
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')
data = data.dropna(subset=columns_to_convert)
data.head()

```

### 计算第5列的均值、中位数、方差、偏度和峰度。将所有结果相加并打印保留两位小数后的结果。
```python
import numpy as np
from scipy import stats
column_5 = data.iloc[:,4]
mean = column_5.mean()
median = column_5.median()
variance = column_5.var()
skewness = column_5.skew()
kurtosis = column_5.kurtosis()
value = sum([mean, median, variance, skewness, kurtosis])
round(value,2)
```

### 对第5列进行Shapiro-Wilk正态性检验。加和Shapiro-Wilk检验统计量和p值，打印保留两位小数后的结果。
```python
from scipy.stats import shapiro
statistic, p_value = stats.shapiro(column_5)
result = statistic + p_value
round(result,2)
```

### 使用 t 检验比较第5列和第6列之间的差异。加和 t 统计量和 p 值，打印保留两位小数后的结果。
```python
from scipy.stats import ttest_ind
column_6 = data.iloc[:, 5]
statistic, p_value = stats.ttest_ind(column_5, column_6)
result = statistic + value
round(result,2)
```

### 对第9列和第10列进行线性回归分析。将斜率、截距、r值、p值和标准误差相加并打印保留两位小数后的结果。
```python
from scipy.stats import linregress
column_9 = data.iloc[:, 8]
column_10 = data.iloc[:, 9]
result = linregress(column_9, column_10)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### 将第5、6、9和10列的所有行进行K均值聚类，得到4个簇。添加一个名为 "Cluster" 的列到数据框中，并用每行所属的类别填充该列。打印索引为15的数据的簇。
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data.iloc[:, [4, 5, 8, 9]]
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```


