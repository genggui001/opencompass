---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: Drink Dataset
  difficulty: Easy
  module: pandas
  idx: 12
  num_steps: 6
  step_types:
    - exec
    - num
    - text
    - num
    - vis
    - num
  modules:
    - pandas
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
    - pandas
---

File Path: `data/drinks.csv`

Load the dataset from the provided path.

```python
import pandas as pd
url = 'data/drinks.csv'
df = pd.read_csv(url)
df.head()
```

Group the dataframe by the continent column. Compute the average beer servings for each continent. Display the first mean value. Keep to 2 decimal places.

```python
grouped = df.groupby('continent')
grouped['beer_servings'].mean()[0].round(2)
```

Find the minimum and maximum wine servings for each continent. Display the resulting dataframe.

```python
grouped['wine_servings'].agg(['min', 'max'])
```

Calculate the total spirit servings in each continent. Display the first value of the resulting series. Keep to 2 decimal places.

```python
grouped['spirit_servings'].sum()[0].round(2)
```


Visualize the average beer servings for each continent. Label the y-axis as 'Mean Beer Servings'.

```python
import matplotlib.pyplot as plt
grouped['beer_servings'].mean().plot(kind='bar')
plt.ylabel('Mean Beer Servings')
plt.show()
```

For a more detailed analysis, group the dataframe by both continent and country columns. Again, compute the mean of all numeric columns in each group of the new grouped dataframe. Display the first mean value of beer_servings. Keep to 2 decimal places.

```python
grouped_two = df.groupby(['continent', 'country'])
grouped_two.mean()['beer_servings'][0].round(2)
```
