---
jupyter:
  title: Analyzing Titanic Passenger Data
  module: seaborn
  dataset: none
  difficulty: MIDDLE
  idx: 1
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - seaborn
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---


Load the built-in dataset 'titanic' from seaborn. Assign it to a DataFrame. Drop the rows with missing values from the dataset.

```python
import seaborn as sns
df = sns.load_dataset('titanic')
df = df.dropna()
```

Create a histogram to show the distribution of 'age' in the dataset.
```python
import matplotlib.pyplot as plt
sns.histplot(data=df, x='age')
plt.show()
```

Create a scatter plot to show the relationship between 'age' and 'fare'.
```python
sns.scatterplot(x='age', y='fare', data=df)
plt.show()
```

Create a swarm plot to show the distribution of 'age' for different passenger classes.
```python
sns.swarmplot(x='pclass', y='age', data=df)
plt.show()
```
