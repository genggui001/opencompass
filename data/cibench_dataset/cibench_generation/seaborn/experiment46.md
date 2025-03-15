---
jupyter:
  title: Visualizing Penguin Dataset using Seaborn and Matplotlib
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 46
  num_steps: 2
  step_types:
    - exec
    - vis
  modules: 
    - seaborn
    - seaborn & matplotlib
---


Load the Penguins dataset from Seaborn.
```python
import seaborn as sns
penguins = sns.load_dataset("penguins")
```

Set the plot style to "whitegrid". Create a new figure for your plot. Set the size to 10x6 to ensure the plot is large enough to clearly display the data. Generate a scatter plot using Seaborn. Set the data to the Penguins dataset, the 'x' and 'y' values to "bill_depth_mm" and "body_mass_g" respectively, the color to 'red', the size to 50, and the marker style to 'x'. Add a title and labels to the scatter plot using Matplotlib. Adjust the font size of the plot elements to 15.
```python
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
sns.scatterplot(data=penguins, x="bill_depth_mm", y="body_mass_g", color='red', size=50, marker='x')
plt.title('Relationship between Bill Depth and Body Mass')
plt.xlabel('Bill Depth (mm)')
plt.ylabel('Body Mass (g)')
plt.rcParams.update({'font.size': 15})
plt.show()
```
