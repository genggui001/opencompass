---
jupyter:
  title: Analyzing The 'tips' Dataset In Joint Plots
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 12
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


Load the 'tips' dataset. We will use seaborn's built-in function.
```python
import seaborn as sns
tips = sns.load_dataset('tips')
```

Create a jointplot to visualize the relationship between 'total_bill' and 'tip' columns using seaborn's jointplot function. Use hexagonal bins instead of scatter points.
```python
import matplotlib.pyplot as plt
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
plt.show()
```

Create a jointplot with Kernel Density Estimation and change the color of the plot to 'red'.
```python
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde', color='red')
plt.show()
```

Change the size ratio to 2 between the scatterplot and the histogram, and hieght to 8. Set the color to 'green' and add a regression line.
```python
sns.jointplot(x='total_bill', y='size', data=tips, ratio=2, height=8, color='green', kind='reg')
plt.show()
```

Change the marker style to x and add a space of 0.5.
```python
sns.jointplot(x='total_bill', y='tip', data=tips, marker='x', space=0.5)
plt.show()
```

Change the color of the histogram bins to 'red'. Specify the number of bins to 15 and fill the bins.
```python
sns.jointplot(x='total_bill', y='tip', data=tips, marginal_kws=dict(bins=15, fill=True, color='red'))
plt.show()
```
