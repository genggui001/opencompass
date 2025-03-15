---
jupyter:
  title: Columns for processing and rows for clustering.
  dataset: Indian Diabetes dataset
  difficulty: Middle
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

File Path : 'data/scipy_dataset02.csv'.

### Load the dataset from the file path and turn it into a pandas dataframe. Get the information of the first 5 rows of data.
```python
import pandas as pd
csv_filename = 'data/scipy_dataset02.csv'
data = pd.read_csv(csv_filename, header = None)
data.head()
```

### Compute the mean, median, variance, skewness, and kurtosis of the 4th column . Add all the results together and print it (rounded to two decimal places).
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

### Compute the Shapiro-Wilk test for the 5th column to check for normality. Calculate the result of the Shapiro-Wilk test statistic plus the p value, print the result (rounded to two decimal places).
```python
from scipy.stats import shapiro
column_5 = data.iloc[:, 4]
statistic, p_value = stats.shapiro(column_5)
result = statistic + p_value
round(result,2)
```

### Use the t-test to compare the difference between the 2nd column and the 3rd column. Calculate the result of the t-statistic plus p-value, print the result (rounded to two decimal places).
```python
from scipy.stats import ttest_ind
column_2 = data.iloc[:, 1]
column_3 = data.iloc[:, 2]
statistic, p_value = stats.ttest_ind(column_2, column_3)
result = statistic + p_value
round(result,2)
```

### Perform linear regression analysis on the 6th column and the 7th column. Add the slope, intercept, r_value, p_value, and standard error together and print the result (rounded to two decimal places).
```python
from scipy.stats import linregress
column_6 = data.iloc[:, 5]
column_7 = data.iloc[:, 6]
result = linregress(column_6, column_7)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### Classify all rows for all the columns into 4 clusters. Please use Kmeans algorithm. Add a column named "Cluster" to the dataframe and fill the column with the class to which each row belongs. Print the cluster of the data with index 15.
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data[[1,2,3,4,5,6,7,8]]
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```
   