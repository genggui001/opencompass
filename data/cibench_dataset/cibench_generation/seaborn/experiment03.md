---
jupyter:
  title: Analyzing and Visualizing the "Penguins" Dataset Using Seaborn
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 3
  num_steps: 5
  step_types:
    - exec
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
---

Load the penguins dataset from Seaborn's built-in datasets.
```python
import seaborn as sns
sns.set()
df = sns.load_dataset("penguins")
df.head()
```

Visualize the distribution of the 'body_mass_g' variable using a histogram. This helps to understand the spread of the body mass of the penguins in grams.
```python
import matplotlib.pyplot as plt
sns.histplot(df['body_mass_g'])
plt.show()
```

Create a scatter plot to visualize the relationship between 'body_mass_g' and 'flipper_length_mm'. Adding a third variable, 'species', for color distinction.
```python
sns.scatterplot(x='body_mass_g', y='flipper_length_mm', hue='species', data=df)
plt.show()
```

Visualize the relationships between all variables, distinguished by 'species'.
```python
sns.pairplot(df, hue='species')
plt.show()
```

Create a line plot to visualize the trend of 'body_mass_g' over the island. Adding a hue semantic to compare the distributions of 'body_mass_g' across different 'species' over the years.
```python
sns.lineplot(x='island', y='body_mass_g', hue='species', data=df)
plt.show()
```
