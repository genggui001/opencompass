---
jupyter:
  title: Columns for processing and rows for clustering.
  dataset: iris dataset
  difficulty: Middle
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

File Path : 'data/scipy_dataset01.csv'.

### Load the dataset from the file path and turn it into a pandas dataframe.  The index of the column should be named after [SepalLength, SepalWidth, PetalLength, PetalWidth, Class] in turn. Get the information of the first 5 rows of data.
```python
import pandas as pd
csv_filename = 'data/scipy_dataset01.csv'
data = pd.read_csv(csv_filename, header=None, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class'])
data.head()
```

### Compute the mean, median, variance, skewness, and kurtosis of the 2nd column 'SepalWidth'. Add all the results together and print it(rounded to two decimal places).
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

### Compute the Shapiro-Wilk test for the 3rd column 'PetalLength' to check for normality. Calculate the result of the Shapiro-Wilk test statistic plus the p value, print the result(rounded to two decimal places).
```python
from scipy.stats import shapiro
column_3 = data["PetalLength"]
statistic, p_value = shapiro(column_3)
result = statistic + p_value
round(result,2)
```

### Use the t-test to compare the difference between the 3rd column and the 4th column 'PetalWidth'. Calculate the result of the t-statistic plus p-value, print the result (rounded to two decimal places).
```python
from scipy.stats import ttest_ind
column_4 = data["PetalWidth"]
t_statistic, p_value = ttest_ind(column_3, column_4)
result = t_statistic + p_value
round(result,2)
```

### Perform linear regression analysis on the 3th column and the 4th column. Add the slope, intercept, r_value, p_value, and standard error together and print the result (rounded to two decimal places).
```python
from scipy.stats import linregress
result = linregress(column_3, column_4)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### Classify all rows for the four columns "SepalLength", "SepalWidth", "PetalLength", "PetalWidth" into 4 clusters. Please use Kmeans algorithm. Add a column named "Cluster" to the dataframe and fill the column with the class to which each row belongs. Print the cluster of the data with index 15.
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```