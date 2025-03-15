---
jupyter:
  title: Visualizing the relationship between total bill and tip using Seaborn's scatterplot
  module: seaborn
  dataset: none
  difficulty: MIDDLE
  idx: 25
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

Load the dataset "tips" from Seaborn's built-in datasets.
```python
import seaborn as sns
tips = sns.load_dataset("tips")
```

Visualize the relationship between the total bill and tip by creating a scatter plot and use the aesthetic style of the plot to "white".
```python
import matplotlib.pyplot as plt
sns.set_style("white")
sns.relplot(x="total_bill", y="tip", data=tips)
plt.show()
```

Change the aesthetic style of the plot to "darkgrid" and recreate the scatter plot.
```python
sns.set_style("darkgrid")
sns.relplot(x="total_bill", y="tip", data=tips)
plt.show()
```


Change the context of the plot to "paper" recreate the scatter plot.
```python
sns.set_context("paper")
sns.relplot(x="total_bill", y="tip", data=tips)
plt.show()
```
