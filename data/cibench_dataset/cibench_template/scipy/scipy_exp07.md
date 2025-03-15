---
jupyter:
  title: Columns for processing and rows for clustering.
  dataset: Wateruse dataset
  difficulty: Middle
  module: scipy
  idx: 7
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


File Path : 'data/scipy_dataset07.csv'.

### Load the dataset from the file path and turn it into a pandas dataframe. Remove rows with non-numeric data in columns ['water_use_k_gals',	'wastewater_use_k_gals',	'total_energy_cost',	'electricity_cost']. Get the information of the first 5 rows of data. 
```python
import pandas as pd
csv_filename = 'data/scipy_dataset07.csv'
data = pd.read_csv(csv_filename, header = 0)
columns_to_convert = ['water_use_k_gals',	'wastewater_use_k_gals',	'total_energy_cost',	'electricity_cost']
data[columns_to_convert] = data[columns_to_convert].apply(pd.to_numeric, errors='coerce')
data = data.dropna(subset=columns_to_convert)
data.head()
```

### Compute the mean, median, variance, skewness, and kurtosis of the 9th column . Add all the results together and print it (rounded to two decimal places).
```python
import numpy as np
from scipy import stats
column_9 = data.iloc[:,8]
mean = column_9.mean()
median = column_9.median()
variance = column_9.var()
skewness = column_9.skew()
kurtosis = column_9.kurtosis()
value = sum([mean, median, variance, skewness, kurtosis])
round(value,2)
```


### Compute the Shapiro-Wilk test for the 9th column to check for normality. Calculate the result of the Shapiro-Wilk test statistic plus the p value, print the result (rounded to two decimal places).
```python
from scipy.stats import shapiro
statistic, p_value = stats.shapiro(column_9)
result = statistic + p_value
round(result,2)
```

### Use the t-test to compare the difference between the 8th column and the 9th column. Calculate the result of the t-statistic plus p-value, print the result (rounded to two decimal places).
```python
from scipy.stats import ttest_ind
column_8 = data.iloc[:, 7]
statistic, p_value = stats.ttest_ind(column_8, column_9)
result = statistic + p_value
round(result,2)
```

### Perform linear regression analysis on the 10th column and the 11th column. Add the slope, intercept, r_value, p_value, and standard error together and print the result (rounded to two decimal places).
```python
from scipy.stats import linregress
column_10 = data.iloc[:, 9]
column_11 = data.iloc[:, 10]
result = linregress(column_10, column_11)
values = sum([result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr])
round(values,2)
```

### Classify all rows for the 8,9,10,11th columns into 4 clusters. Please use Kmeans algorithm. Remember to convert the numeric type of column to float. Add a column named "Cluster" to the dataframe and fill the column with the class to which each row belongs. Print the cluster of the data with index 15.
```python
from scipy.cluster.vq import kmeans, vq
num_clusters = 4
data_for_clustering = data.iloc[:, [7, 8, 9, 10]].astype(float)
centroids, _ = kmeans(data_for_clustering.values, num_clusters)
cluster_labels, _ = vq(data_for_clustering.values, centroids)
data["Cluster"] = cluster_labels
print(data.iloc[14]["Cluster"])
```

