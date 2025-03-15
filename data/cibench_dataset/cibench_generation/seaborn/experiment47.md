---
jupyter:
  title: Using PairGrid for Iris Dataset Visualization
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 47
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


Load the Iris dataset from Seaborn library.
```python
import seaborn as sns
iris = sns.load_dataset('iris')
```

Customize the PairGrid by mapping different types of plots to different positions. We put histogram plots on the diagonal and scatter plots off the diagonal.
```python
import matplotlib.pyplot as plt
g = sns.PairGrid(iris)
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)
plt.show()
```

Further customize the PairGrid by coloring the plots by species and adds a legend to the plot.
```python
g = sns.PairGrid(iris, hue="species")
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)
g = g.add_legend()
plt.show()
```

Customize the PairGrid by making different types of plots in the lower and upper triangles. We map scatter plots to the upper triangle and kernel density estimation (kde) plots to the lower triangle and the diagonal.
```python
g = sns.PairGrid(iris, hue="species")
g = g.map_upper(plt.scatter)
g = g.map_lower(sns.kdeplot)
g = g.map_diag(sns.kdeplot, lw=3, legend=False)
g = g.add_legend()
plt.show()
```

Customize the PairGrid by choosing specific variable pairings. Here, we are only interested in the relationship between "sepal_length" and "sepal_width".
```python
g = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"], hue="species")
g = g.map(plt.scatter)
g = g.add_legend()
plt.show()
```

Customize the appearance of the PairGrid itself. We set the color palette to "Set2" and use different markers for different species. We also set the line widths, edge color, and size of the markers for the scatter plots.
```python
g = sns.PairGrid(iris, hue="species", palette="Set2", hue_kws={"marker": ["o", "s", "D"]})
g = g.map(plt.scatter, linewidths=1, edgecolor="w", s=40)
g = g.add_legend()
plt.show()
```