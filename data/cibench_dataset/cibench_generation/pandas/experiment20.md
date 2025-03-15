---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Airbnb New York City dataset
  difficulty: Easy
  module: pandas
  idx: 20
  num_steps: 7
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
    - exec
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas & matplotlib
---

File Path: `data/AB_NYC_2019.csv`


Load the Airbnb New York City dataset into a pandas dataframe.
```python
import pandas as pd
df = pd.read_csv('data/AB_NYC_2019.csv')
df.head()
```

For measuring the execution time of different functions, create a reusable function named 'measure_time'. This function should take another function as an argument, record the time before and after its execution, and return the difference. Compute the mean price of the Airbnb listings. First, create a custom function named 'custom_mean' that sums up all the prices and divides by the total number of prices. Use the measure_time function to calculate its execution time. Then, compare this with the execution time of the built-in mean() function of pandas. Keep to 2 decimal places. Display the difference in execution times.
```python
from timeit import default_timer as timer
def measure_time(func):
    start = timer()
    func()
    end = timer()
    return end - start
def custom_mean():
    return sum(df['price'])/len(df['price'])

round(measure_time(custom_mean) - measure_time(df['price'].mean), 2)
```

Convert the prices from dollars to euros assuming the exchange rate is 0.85. Two methods are compared here: using a loop and using vectorization. The respective execution times are measured using the measure_time function. Keep to 2 decimal places. Display the difference in execution times.
```python
def loop_conversion():
    df['price_euro'] = [price*0.85 for price in df['price']]

def vectorized_conversion():
    df['price_euro'] = df['price']*0.85
round(measure_time(loop_conversion) - measure_time(vectorized_conversion),2)
```

Compute the mean price for each neighbourhood group in Manhattan. First, use a chain of operations to filter the data and calculate the mean. Measure its execution time. Then, perform the same operation using a single operation and measure its execution time. Keep to 2 decimal places. Display the difference in execution times.
```python
def chain_operations():
    return df[df['neighbourhood_group']=='Manhattan']['price'].mean()

def single_operation():
    return df.loc[df['neighbourhood_group']=='Manhattan', 'price'].mean()
round(measure_time(chain_operations) - measure_time(single_operation), 2)
```

Change the data type of the 'neighbourhood_group' column from 'object' to 'category' for better efficiency. Then, measure the time it takes to get its unique values. Keep to 2 decimal places.
```python
df['neighbourhood_group'] = df['neighbourhood_group'].astype('category')
round(measure_time(df['neighbourhood_group'].unique),2)
```

Finally, compute the mean price for each neighbourhood group using the groupby method and measure the execution time. Keep to 2 decimal places.
```python
round(measure_time(df.groupby('neighbourhood_group')['price'].mean),2)
```

For a visual understanding of the mean price distribution, plot a bar graph of the mean price for each neighbourhood group. Use the plot() method of pandas dataframe with 'kind' parameter set to 'bar'. Label the y-axis as 'Mean Price'.
```python
import matplotlib.pyplot as plt
df.groupby('neighbourhood_group')['price'].mean().plot(kind='bar')
plt.ylabel('Mean Price')
plt.show()
```