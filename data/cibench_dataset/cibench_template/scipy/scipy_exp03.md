---
jupyter:
  title: Columns for processing and rows for clustering.
  dataset: crash dataset
  difficulty: Middle
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

File Path : 'data/scipy_dataset03.csv'.

### Load the dataset from the file path and turn it into a pandas dataframe. Remove rows with non-numeric data in columns ['MUNICIPALITY','POLICE_AGCY','TIME_OF_DAY','HOUR_OF_DAY']. Get the information of the first 5 rows of data. 
```python
import pandas as pd
csv_filename = 'data/scipy_dataset03.csv'
data = pd.read_csv(csv_filename, header = 0)
columns_to_convert = ['MUNICIPALITY','POLICE_AGCY','TIME_OF_DAY','HOUR_OF_DAY']
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')
data = data.dropna(subset=columns_to_convert)
data.head()

```

### Compute the mean, median, variance, skewness, and kurtosis of the 5th column . Add all the results together and print it (rounded to two decimal places).
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

### Compute the Shapiro-Wilk test for the 5th column to check for normality. Calculate the result of the Shapiro-Wilk test statistic plus the p value, print the result (rounded to two decimal places).
```python
from scipy.stats import shapiro
statistic, p_value = stats.shapiro(column_5)
result = statistic + p_value
round(result,2)
```

### Use the t-test to compare the difference between the 5th column and the 6th column. Calculate the result of the t-statistic plus p-value, print the result (rounded to two decimal places).
```python
from scipy.stats import ttest_ind
column_6 = data.iloc[:, 5]
statistic, p_value = stats.ttest_ind(column_5, column_6)
result = statistic + p_value
round(result,2)
```

### Perform linear regression analysis on the 9th column and the 10th column. Add the slope, intercept, r_value, p_value, and standard error together and print the result (rounded to two decimal places).
```python
from scipy.stats import linregress
column_9 = data.iloc[:, 8]
column_10 = data.iloc[:, 9]
result = linregress(column_9, column_10)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### Classify all rows for the 5th,6th,9th and 10th columns into 4 clusters. Please use Kmeans algorithm. Add a column named "Cluster" to the dataframe and fill the column with the class to which each row belongs. Print the cluster of the data with index 15 (rounded to two decimal places).
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data.iloc[:, [4, 5, 8, 9]]
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```


