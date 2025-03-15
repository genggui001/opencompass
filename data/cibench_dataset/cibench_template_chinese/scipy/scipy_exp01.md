---
jupyter:
  title: 列处理和行聚类
  dataset: 鸢尾花数据集
  difficulty: 中级
  module: scipy
  idx: 1
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


文件路径：'data/scipy_dataset01.csv'.
### 从文件路径加载数据集并转换为 pandas 数据框。列的索引应依次命名为 [SepalLength, SepalWidth, PetalLength, PetalWidth, Class]。获取前5行数据的信息。
```python
import pandas as pd
csv_filename = 'data/scipy_dataset01.csv'
data = pd.read_csv(csv_filename, header=None, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class'])
data.head()
```

### 计算第2列 'SepalWidth' 的均值、中位数、方差、偏度和峰度。将所有结果相加并打印保留两位小数后的结果。
```python
import numpy as np
from scipy import stats
column_2 = data['SepalWidth']
mean = np.mean(column_2)
median = np.median(column_2)
variance = np.var(column_2)
skewness = stats.skew(column_2)
kurtosis = stats.kurtosis(column_2)
value = sum([mean, median, variance, skewness, kurtosis])
round(value,2)
```

### 对第3列 'PetalLength' 进行Shapiro-Wilk正态性检验。将Shapiro-Wilk检验统计量和p值加和，打印保留两位小数后的结果。
```python
from scipy.stats import shapiro
column_3 = data["PetalLength"]
statistic, p_value = shapiro(column_3)
result = statistic + p_value
round(result,2)
```

### 使用 t 检验比较第3列和第4列 'PetalWidth' 之间的差异。将 t 统计量和 p 值加和，打印保留两位小数后的结果。
```python
from scipy.stats import ttest_ind
column_4 = data["PetalWidth"]
t_statistic, p_value = ttest_ind(column_3, column_4)
result = t_statistic + p_value
round(result,2)
```

### 对第3列和第4列进行线性回归分析。将斜率、截距、r值、p值和标准误差相加并打印保留两位小数后的结果。
```python
from scipy.stats import linregress
result = linregress(column_3, column_4)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### 将四列 "SepalLength", "SepalWidth", "PetalLength", "PetalWidth" 中的所有行进行K均值聚类，得到4个簇。添加一个名为 "Cluster" 的列到数据框中，并用每行所属的类别填充该列。打印索引为15的数据的簇。
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```