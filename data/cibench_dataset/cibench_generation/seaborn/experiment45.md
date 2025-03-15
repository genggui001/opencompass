---
jupyter:
  title: Analyzing Penguins Dataset with Seaborn
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 45
  num_steps: 7
  step_types:
    - exec
    - vis
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
    - seaborn & matplotlib
---

Load the penguins dataset from the seaborn library.
```python
import seaborn as sns
penguins = sns.load_dataset("penguins")
```

Create a JointGrid with seaborn. Set "bill_length_mm" as the x variable and "bill_depth_mm" as the y variable. Plot a scatter diagram of bill length against bill depth, and a histogram of each on the initialized JointGrid.
```python
import matplotlib.pyplot as plt
g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot(sns.scatterplot, sns.histplot)
plt.show()
```

Plot a scatter diagram on the joint axes of the JointGrid. Plot the marginal distributions of bill length and bill depth on the marginal axes of the JointGrid using a histogram with a kernel density estimate (kde).
```python
g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.scatterplot, color=".5")
g.plot_marginals(sns.histplot, kde=True)
plt.show()
```

Plot a bivariate hexbin diagram, a type of histogram used for bivariate data, with marginal histograms. Set the space parameter to 0 to have no space between the joint and marginal plots.
```python
g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm", space=0)
g.plot_joint(plt.hexbin, color="b")
g.plot_marginals(sns.histplot, kde=False, color="b")
plt.show()
```

Plot a scatter diagram with bill length and bill depth as variables in the joint axes, a histogram of bill length in the x marginal axis, and a KDE of bill depth in the y marginal axis.
```python
g = sns.JointGrid()
x, y = penguins["bill_length_mm"], penguins["bill_depth_mm"]
sns.scatterplot(x=x, y=y, ec="b", fc="none", s=100, linewidth=1.5, ax=g.ax_joint)
sns.histplot(x=x, fill=False, linewidth=2, ax=g.ax_marg_x)
sns.kdeplot(y=y, linewidth=2, ax=g.ax_marg_y)
plt.show()
```

Plot a bivariate histogram with marginal boxplots. Boxplots provide a visual summary of the data through their quartiles.
```python
g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.kdeplot, fill=True)
g.plot_marginals(sns.violinplot)
plt.show()
```

Plot a bivariate scatterplot with marginal density plots.
```python
g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.scatterplot)
g.plot_marginals(sns.kdeplot, fill=True)
plt.show()
```