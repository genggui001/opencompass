---
jupyter:
  title: Analyze the 'penguins' dataset from the Seaborn
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 37
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

Load the 'penguins' dataset using seaborn's built-in function. If there are any null values, remove the corresponding rows from the dataset.
```python
import seaborn as sns
penguins = sns.load_dataset("penguins")
penguins = penguins.dropna()
```

Create a boxenplot for the 'bill_length_mm' column, grouped by 'species'.
```python
import matplotlib.pyplot as plt
sns.boxenplot(x='species', y='bill_length_mm', data=penguins)
plt.show()
```


Create a horizontal boxenplot for the 'bill_length_mm' column, grouped by 'species'. Set palette to Set3
```python
sns.boxenplot(x='bill_length_mm', y='species', data=penguins, palette="Set3")
plt.show()
```

Lastly, add a title to the boxenplot and set the figure size to 10, 6 for better readability.
```python
plt.figure(figsize=(10,6))
sns.boxenplot(x='bill_length_mm', y='species', data=penguins, palette="Set3")
plt.title('Boxenplot of Penguin Bill Length by Species')
plt.show()
```