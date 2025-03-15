---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: wine quality dataset
  difficulty: Easy
  module: pandas
  idx: 30
  num_steps: 4
  step_types:
    - exec
    - text
    - text
    - vis
  modules:
    - pandas
    - pandas&sklearn
    - pandas&sklearn
    - pandas&matplotlib
---

File Path: `data/winequality-red.csv`

Load the 'Vinho Verde' wine dataset from the provided path into a pandas DataFrame.
```python
import pandas as pd
url = 'data/winequality-red.csv'
df = pd.read_csv(url)
df.head()
```

Standardize the 'alcohol' column using sklearn's preprocessing.scale function. Add this standardized data as a new column named 'scaled_alcohol' in the dataframe. Display the scaled data to verify that it has been standardized.
```python
from sklearn import preprocessing
df['scaled_alcohol'] = preprocessing.scale(df['alcohol'])
df['scaled_alcohol']
```

Normalize the 'alcohol' column using sklearn's preprocessing.MinMaxScaler function. This will transform the data to have a range between 0 and 1. Add this normalized data as a new column named 'normalized_alcohol' in the dataframe.
```python
min_max_scaler = preprocessing.MinMaxScaler()
df['normalized_alcohol'] = min_max_scaler.fit_transform(df[['alcohol']])
df['normalized_alcohol']
```

To visualize the effect of standardization and normalization, plot histograms of the original 'alcohol' data, the standardized 'scaled_alcohol' data, and the normalized 'normalized_alcohol' data.
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.hist(df['alcohol'], bins=30)
plt.title('Original Data')

plt.subplot(132)
plt.hist(df['scaled_alcohol'], bins=30)
plt.title('Standard Scaled Data')

plt.subplot(133)
plt.hist(df['normalized_alcohol'], bins=30)
plt.title('Min-Max Normalized Data')

plt.show()
```