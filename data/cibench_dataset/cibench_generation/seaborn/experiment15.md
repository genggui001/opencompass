---
jupyter:
  title: Visualizing the Tips Dataset Using Seaborn and Matplotlib
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 15
  num_steps: 6
  step_types:
    - text
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


Load the 'tips' dataset from seaborn into a dataframe called 'tips'.
```python
import seaborn as sns
tips = sns.load_dataset('tips')
```

You can create a basic linear regression plot between 'total_bill' and 'tip' with height 7.
```python
import matplotlib.pyplot as plt
sns.lmplot(data=tips, x='total_bill', y='tip', height=7)
plt.show()
```

You can color the points on the plot according to the 'smoker' status. Change the marker style of points on the plot to 'o' and 'v'.
```python
sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker', markers=['o', 'v'])
plt.show()
```

Split the plot into multiple columns according to the 'time' variable.Split the plot into multiple rows according to the 'sex' variable.
```python
sns.lmplot(data=tips, x='total_bill', y='tip', hue='smoker', col='time', row='sex')
plt.show()
```

Add regression lines for each category of 'day' by setting 'hue', 'col' and 'row' parameters to 'day', 'day', and 'sex' respectively with coolwarm palette.
```python
sns.lmplot(data=tips, x='total_bill', y='tip', hue='day', col='day', row='sex', palette='coolwarm')
plt.show()
```

Add jitter of 0.1 to the scatter plot and set aspect to 1.
```python
sns.lmplot(x='size', y='total_bill', data=tips, hue='smoker', palette='coolwarm', aspect=1, x_jitter=.1)
plt.show()
```