---
jupyter:
  title: Analyzing Penguins Dataset Using Seaborn and Matplotlib
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 34
  num_steps: 5
  step_types:
    - exec
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
---

Load the Penguins dataset provided by Seaborn. Drop the rows containing missing data from the dataset.
```python
import seaborn as sns
penguins = sns.load_dataset("penguins")
penguins = penguins.dropna()
```

Plot a univariate distribution of observations for the 'flipper_length_mm' column. Add color to the plot based on the 'species' column to differentiate between the species.
```python
import matplotlib.pyplot as plt
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species")
plt.show()
```

Fill the area under the lines of the plot with color for better visualization. Calculate the mean of the 'flipper_length_mm' column and add a vertical line to the plot at this mean value.
```python 
mean_fl = penguins['flipper_length_mm'].mean()
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", fill=True)
plt.axvline(mean_fl, color='red', linestyle='--')
plt.show()
```

Plot a bivariate distribution of 'flipper_length_mm' and 'body_mass_g' columns.Color the bivariate plot based on the 'species' column to differentiate between the species.
```python
sns.kdeplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.show()
```

Fill the area under the lines of the bivariate plot with color for better visualization. Add a legend to the plot using 'species' as the title.
```python
sns.kdeplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", fill=True)
plt.legend(title='Species')
plt.show()
```
