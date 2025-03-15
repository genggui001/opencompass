---
jupyter:
  title: Visualizing the Titanic Dataset with Seaborn
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 44
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

Load the Titanic dataset which is an inbuilt dataset in the seaborn library.
```python
import seaborn as sns
titanic = sns.load_dataset('titanic')
```

Create a FacetGrid object for the column 'sex'. Create a histogram of the 'age' column for each facet.
```python
import matplotlib.pyplot as plt
g = sns.FacetGrid(titanic, col='sex')
g = g.map(plt.hist, 'age')
plt.show()
```

Create another FacetGrid for the columns 'sex' and 'class'.Plot a histogram of the 'age' column for each facet of this new FacetGrid. This gives a visualization of the distribution of ages for each combination of 'sex' and 'class'.
```python
g = sns.FacetGrid(titanic, col='sex', row='class')
g = g.map(plt.hist, 'age')
plt.show()
```

Add padding between the plots, set the color of the histograms to 'skyblue', add titles to each subplot, and remove the spines on the left side of the plots.Finally, display the modified plot. This plot provides a clear and visually appealing representation of the distribution of ages among different classes and sexes.
```python
g = sns.FacetGrid(titanic, col='sex', row='class', margin_titles=True, despine=False)
g = (g.map(plt.hist, 'age', color='skyblue').set_titles("{col_name} {col_var}").despine(left=True))
plt.show()
```
