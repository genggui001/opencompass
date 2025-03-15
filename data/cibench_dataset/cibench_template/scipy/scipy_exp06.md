---
jupyter:
  title: Columns for processing and rows for clustering.
  dataset: Arrest dataset
  difficulty: Middle
  module: scipy
  idx: 6
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

File Path : 'data/scipy_dataset06.csv'.

### Load the dataset from the file path and turn it into a pandas dataframe. Remove rows with non-numeric data in columns ['AGE', 'INCIDENTZONE',	'INCIDENTTRACT',	'COUNCIL_DISTRICT']. Get the information of the first 5 rows of data. 
```python
import pandas as pd
csv_filename = 'data/scipy_dataset06.csv'
data = pd.read_csv(csv_filename, header = 0)
columns_to_convert = ['AGE', 'INCIDENTZONE',	'INCIDENTTRACT',	'COUNCIL_DISTRICT']
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')
data = data.dropna(subset=columns_to_convert)
data.head()
```

### Compute the mean, median, variance, skewness, and kurtosis of the 4th column . Add all the results together and print it (rounded to two decimal places).
```python
import numpy as np
from scipy import stats
column_4 = data.iloc[:,3]
mean = column_4.mean()
median = column_4.median()
variance = column_4.var()
skewness = column_4.skew()
kurtosis = column_4.kurtosis()
value = sum([mean, median, variance, skewness, kurtosis])
round(value,2)
```

### Compute the Shapiro-Wilk test for the 4th column to check for normality. Calculate the result of the Shapiro-Wilk test statistic plus the p value, print the result (rounded to two decimal places).
```python
from scipy.stats import shapiro
statistic, p_value = stats.shapiro(column_4)
result = statistic + p_value
round(result,2)
```

### Use the t-test to compare the difference between the 4th column and the 12th column. Calculate the result of the t-statistic plus p-value, print the result (rounded to two decimal places).
```python
from scipy.stats import ttest_ind
column_12 = data.iloc[:, 11]
statistic, p_value = stats.ttest_ind(column_4, column_12)
result = statistic + p_value
round(result,2)
```

### Perform linear regression analysis on the 4th column and the 13th column. Add the slope, intercept, r_value, p_value, and standard error together and print the result (rounded to two decimal places).
```python
from scipy.stats import linregress
column_13 = data.iloc[:, 12]
result = linregress(column_4, column_13)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### Classify all rows for the 4th,12th,13th and 14th columns into 4 clusters. Please use Kmeans algorithm. Remember to convert the numeric type of column to float. Add a column named "Cluster" to the dataframe and fill the column with the class to which each row belongs. Print the cluster of the data with index 15.
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data.iloc[:, [3, 11, 12, 13]].astype(float)
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```
