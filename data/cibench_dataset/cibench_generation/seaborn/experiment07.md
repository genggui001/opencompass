---
jupyter:
  title: Data Visualization of the 'tips' Dataset using Seaborn and Matplotlib Libraries in Python
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 7
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

File Path: none. 



Load the 'tips' dataset from the seaborn library.
```python
import seaborn as sns
tips = sns.load_dataset('tips')
```

Let us visualize the count of each category in the 'day' column using a bar plot. Change the color to blue.
```python
import matplotlib.pyplot as plt
sns.countplot(x='day', data=tips, palette='Blues')
plt.show()
```

Create a box plot can be used to visualize the distribution of 'total_bill' for each 'day'. Add a nested categorical variable 'smoker' to the box plot.
```python
sns.boxplot(x='day', y='total_bill', hue='smoker', data=tips)
plt.show()
```


Create a violin plot to visualize the distribution and density of 'total_bill' for each 'day'.Add a nested categorical variable 'smoker' to the violin plot.
```python
sns.violinplot(x='day', y='total_bill', hue='smoker', data=tips)
plt.show()
```

Create a strip plot to visualize the distribution of 'total_bill' for each 'day'. Add a nested categorical variable 'smoker' to the strip plot.
```python
sns.stripplot(x='day', y='total_bill', hue='smoker', data=tips)
plt.show()
```

Create a swarm plot to visualize the distribution of 'total_bill' for each 'day' with no overlapping points. Add a nested categorical variable 'smoker' to the swarm plot.
```python
sns.swarmplot(x='day', y='total_bill', hue='smoker', data=tips)
plt.show()
```