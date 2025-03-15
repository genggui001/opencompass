---
jupyter:
  title: Analyzing the 'flights' and 'tips' datasets from the seaborn
  module: seaborn
  dataset: none
  difficulty: MIDDLE
  idx: 27
  num_steps: 6
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - seaborn
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---

Load the 'flights' dataset from seaborn's built-in datasets. Transform the 'flights' dataset into a pivot table. Set 'month' as the index, 'year' as the columns, and 'passengers' as the values.
```python
import seaborn as sns
flights = sns.load_dataset('flights')
pivot_flights = flights.pivot_table(index='month', columns='year', values='passengers')
```

Generate a heatmap of the pivot table to visualize the number of passengers over time. Adding a color map named 'YlGnBu' and a white divider between the squares.
```python
import matplotlib.pyplot as plt
sns.heatmap(pivot_flights, cmap='YlGnBu', linecolor='white', linewidths=1)
plt.show()
```

Generate a cluster map of the pivot table to visualize the relationships between different months and years. Adding a color map named 'coolwarm' and standardize the scale to 1.
```python
sns.clustermap(pivot_flights, cmap='coolwarm', standard_scale=1)
plt.show()
```

Load the 'tips' dataset from seaborn's built-in datasets. Calculate the correlation matrix of the 'tips' dataset to quantify the relationships between variables. Generate a heatmap of the correlation matrix to visualize the correlations between different variables in the 'tips' dataset.
```python
tips = sns.load_dataset('tips')
tips.head()
tips_corr = tips.corr()
tips_corr
sns.heatmap(tips_corr, annot=True, cmap='coolwarm')
plt.show()
```

Create a pair grid of the 'tips' dataset to visualize pairwise relationships between variables. Assigning different plots to the upper (scatter plot), lower (KDE plot), and diagonal sections (histogram). Also, add a legend for 'sex'
```python
pair_grid = sns.PairGrid(tips, hue='sex')
pair_grid.map_upper(plt.scatter)
pair_grid.map_lower(sns.kdeplot)
pair_grid.map_diag(sns.histplot)
pair_grid.add_legend()
plt.show()
```

Generate a facet grid of the 'tips' dataset with 'time' as columns, 'smoker' as rows, and 'total_bill' as the histogram variable.
```python
facet_grid = sns.FacetGrid(tips, col='time', row='smoker')
facet_grid.map(plt.hist, 'total_bill')
plt.show()
```
