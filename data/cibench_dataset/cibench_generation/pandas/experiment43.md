---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Tips Dataset
  difficulty: Easy
  module: pandas
  idx: 43
  num_steps: 5
  step_types:
    - exec
    - text
    - vis
    - text
    - text
  modules:
    - pandas
    - pandas
    - pandas&matplotlib
    - pandas&numpy
    - pandas
---

File Path: `data/tips.csv`

Load the dataset from the provided path. Store the data in a dataframe named 'tips'.

```python
import pandas as pd
url = 'data/tips.csv'
tips = pd.read_csv(url)
tips.head()
```

Group the data by 'sex' and 'smoker' columns using the groupby function and calculate the mean of 'total_bill' for each group.
```python
tips.groupby(['sex', 'smoker'])['total_bill'].mean()
```

Create a new column 'tip_percentage' to understand the tipping behavior of customers. This column calculates the percentage of the 'tip' to the 'total_bill'. This is done by dividing the 'tip' column by the 'total_bill' column and multiplying the result by 100. Visualize the distribution of tip percentages by creating a histogram of the 'tip_percentage' column using the plot function with kind set to 'hist' and rwidth set to 0.8. Label the x-axis as 'Tip Percentage'
```python
import matplotlib.pyplot as plt

tips['tip_percentage'] = tips['tip'] / tips['total_bill'] * 100
tips['tip_percentage'].plot(kind='hist', rwidth=0.8)
plt.xlabel('Tip Percentage')
plt.show()
```

For analysis of high value bills, filter the data to only include rows where 'total_bill' is more than 40. This is done by using a boolean mask to filter the dataframe. Transform the data for better statistical analysis by applying the numpy function 'log1p' to the 'total_bill' column. This function applies a natural logarithmic function to 1 plus the input array, effectively scaling down the values in the 'total_bill' column while maintaining their distribution.
```python
tips[tips['total_bill'] > 40]
import numpy as np
tips['total_bill'].apply(np.log1p)
```

Analyze trends in the data by creating a pivot table that shows the mean 'total_bill' for each 'sex' and 'day'. This is done by using the pivot_table function with values set to 'total_bill', index set to 'sex', columns set to 'day', and aggfunc set to numpy's mean function.
```python
pd.pivot_table(tips, values='total_bill', index='sex', columns='day', aggfunc=np.mean)
```