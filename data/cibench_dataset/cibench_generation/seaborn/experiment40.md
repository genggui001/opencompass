---
jupyter:
  title: Analyzing 'tips' dataset using linear regression and residual plots
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 40
  num_steps: 3
  step_types:
    - exec
    - vis
    - vis
  modules: 
    - seaborn
    - seaborn & matplotlib
    - seaborn & matplotlib
---

Load the tips dataset from seaborn. 
```python
import seaborn as sns
tips = sns.load_dataset("tips")
```

Create a residual plot with order 2.
```python
import matplotlib.pyplot as plt
sns.residplot(x="total_bill", y="tip", data=tips, order=2)
plt.show()
```

Create a residual plot with scatter kwargs with s 80 and red color.
```python
sns.residplot(x="total_bill", y="tip", data=tips, scatter_kws={"s": 80, "color": "red"})
plt.show()
```
