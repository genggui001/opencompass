---
jupyter:
  title: Visualizing Titanic Dataset From Seaborn With Pointplots
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 21
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

Load the Titanic dataset from seaborn's built-in.
```python
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()
```

Generate a basic pointplot between class and survived. Add another sex dimension to the plot.
```python
import matplotlib.pyplot as plt
sns.pointplot(x='class', y='survived', hue='sex', data=titanic)
plt.show()
```

Change ["^", "o"] for markers and ["-", "--"] for line styles. 
```python
sns.pointplot(x='class', y='survived', hue='sex', data=titanic, markers=["^", "o"], linestyles=["-", "--"])
plt.show()
```

Alter the order of classes to ['First', 'Third', 'Second']. Set palette to Set2
```python
sns.pointplot(x='class', y='survived', hue='who', data=titanic, palette="Set2", order=['First', 'Third', 'Second'])
plt.show()
```

Use seaborn's 'catplot' function to draw a pointplot on different variables for rows and columns. Set 'sex' as the x-axis, 'survived' as the y-axis, and 'class' as the hue.
```python
sns.catplot(x='sex', y='survived', hue='class', kind='point', data=titanic)
plt.show()
```

Apply a different color palette for the pointplot. For instance, use the 'deep' color palette.
```python
sns.catplot(x='survived', y='class', hue='sex', palette='deep', kind='point', data=titanic)
plt.show()
```