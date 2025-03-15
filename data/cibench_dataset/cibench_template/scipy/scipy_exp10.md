---
jupyter:
  title: Columns for processing and rows for clustering.
  dataset: MonthlyDeaths dataset
  difficulty: Middle
  module: scipy
  idx: 10
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

File Path : 'data/scipy_dataset10.csv'.

### Load the dataset from the file path and turn it into a pandas dataframe. Remove rows with non-numeric data in columns ['Malignant Neoplasms',	'Diabetes Mellitus',	'Alzheimer Disease',	'Influenza and Pneumonia']. Get the information of the first 5 rows of data. 
```python
import pandas as pd
csv_filename = 'data/scipy_dataset10.csv'
data = pd.read_csv(csv_filename, header = 0)
columns_to_convert = ['Malignant Neoplasms',	'Diabetes Mellitus',	'Alzheimer Disease',	'Influenza and Pneumonia']
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')
data = data.dropna(subset=columns_to_convert)
data.head()
```

### Compute the mean, median, variance, skewness, and kurtosis of the 6th column . Add all the results together and print it (rounded to two decimal places).
```python
import numpy as np
from scipy import stats
column_6 = data.iloc[:,5]
mean = column_6.mean()
median = column_6.median()
variance = column_6.var()
skewness = column_6.skew()
kurtosis = column_6.kurtosis()
value = sum([mean, median, variance, skewness, kurtosis])
round(value,2)
```

### Compute the Shapiro-Wilk test for the 6th column to check for normality. Calculate the result of the Shapiro-Wilk test statistic plus the p value, print the result (rounded to two decimal places).
```python
from scipy.stats import shapiro
statistic, p_value = stats.shapiro(column_6)
result = statistic + p_value
round(result,2)
```

### Use the t-test to compare the difference between the 6th column and the 7th column. Calculate the result of the t-statistic plus p-value, print the result (rounded to two decimal places).
```python
from scipy.stats import ttest_ind
column_7 = data.iloc[:, 6]
statistic, p_value = stats.ttest_ind(column_6, column_7)
result = statistic + p_value
round(result,2)
```

### Perform linear regression analysis on the 8th column and the 9th column. Add the slope, intercept, r_value, p_value, and standard error together and print the result (rounded to two decimal places).
```python
from scipy.stats import linregress
column_8 = data.iloc[:, 7]
column_9 = data.iloc[:, 8]
result = linregress(column_8, column_9)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### Classify all rows for the 6,7,8,9th columns into 4 clusters. Please use Kmeans algorithm. Remember to convert the numeric type of column to float. Add a column named "Cluster" to the dataframe and fill the column with the class to which each row belongs. Print the cluster of the data with index 15.
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data.iloc[:, [5,6,7,8]].astype(float)
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```

  