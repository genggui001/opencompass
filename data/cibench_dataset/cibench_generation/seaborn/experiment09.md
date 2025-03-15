---
jupyter:
  title: Analyzing The 'tips' Dataset In Violin Plots
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 9
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


Load the 'tips' dataset from seaborn into a pandas dataframe.
```python
import seaborn as sns
tips = sns.load_dataset('tips')
```

Create a vertical violin plot for the 'total_bill' column.
```python
import matplotlib.pyplot as plt
sns.violinplot(y=tips["total_bill"])
plt.show()
```

Create a split violin plot for the 'total_bill' column, split by 'day' and colored by 'sex'.
```python
sns.violinplot(x='day', y='total_bill', hue='sex', split=True, data=tips)
plt.show()
```

Display quartile values inside the violins by setting the 'inner' parameter to "quartile". Set scale to count.
```python
sns.violinplot(x='day', y='total_bill', hue='sex', split=True, inner="quartile", scale="count", data=tips)
plt.show()
```

Set order to ['Thur','Fri','Sat','Sun'] to display the violins in this order and set 'palette' parameter to "Set3". Draw the violin plot on a specific Axes by using the 'ax' parameter. This can be done by first creating a subplot and then passing the ax object to the 'ax' parameter.
```python
fig, ax = plt.subplots()
sns.violinplot(ax=ax, x='day', y='total_bill', hue='sex', split=True, inner="quartile", scale="count", order=['Thur','Fri','Sat','Sun'], palette="Set3", data=tips)
plt.show()
```

Combine a violin plot with a swarm plot for better visualization.
```python
sns.violinplot(x='day', y='total_bill', data=tips, inner=None)
sns.swarmplot(x='day', y='total_bill', data=tips, color='white', edgecolor='gray')
plt.show()
```
