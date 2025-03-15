---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: drinks Dataset
  difficulty: Easy
  module: pandas
  idx: 16
  num_steps: 5
  step_types:
    - exec
    - vis
    - num
    - vis
    - vis
  modules:
    - pandas
    - pandas&matplotlib
    - pandas
    - pandas&matplotlib
    - pandas&matplotlib
---

File Path: `data/drinks.csv`

Load the dataset from the given URL into a pandas DataFrame. Check the first five rows of the DataFrame
```python
import pandas as pd
url = 'data/drinks.csv'
df = pd.read_csv(url)
df.head()
```

Calculate the pairwise correlation of numerical columns, excluding NA/null values. Visualize this correlation matrix.
```python
# numerical columns
import matplotlib.pyplot as plt
df_num = df.select_dtypes(include=['number'])
correlation = df_num.corr()
plt.imshow(correlation, cmap='viridis')
plt.colorbar()
plt.xticks(range(len(correlation)), correlation.columns, rotation=20)
plt.yticks(range(len(correlation)), correlation.columns)
plt.show()
```

Count the number of countries in each continent. Display the maximum number of countries in a continent.
```python
continent_counts = df['continent'].value_counts()
continent_counts.max()
```

To visualize the distribution of countries across continents, plot a pie chart.
```python
plt.pie(continent_counts, labels = continent_counts.index, autopct='%1.1f%%')
plt.title('Countries per Continent')
plt.show()
```

Group the DataFrame by 'continent' and calculate the total beer_servings for each continent. Then, plot a bar chart to visualize the result.
```python
beer_sum = df.groupby('continent')['beer_servings'].sum()
beer_sum.plot(kind='bar')
plt.ylabel('Total Beer Servings')
plt.title('Total Beer Servings By Continent')
plt.show()
```

