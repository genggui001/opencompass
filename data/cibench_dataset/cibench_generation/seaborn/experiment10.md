---
jupyter:
  title: Visualizing Flight Data Using Heatmaps in Python
  module: seaborn
  dataset: none
  difficulty: MIDDLE
  idx: 10
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


Load the 'flights' built-in dataset from seaborn. Set 'month' as the index, 'year' as the columns, and 'passengers' as the values.
```python
import seaborn as sns
flights = sns.load_dataset('flights')
flights = flights.pivot(index='month', columns='year', values='passengers')
```

Generate a basic heatmap and add annotations to the heatmap for better understanding of the data. Display numbers in decimal format. Change the color map of the heatmap to 'YlGnBu' to enhance the visual appeal.
```python
import matplotlib.pyplot as plt
sns.heatmap(flights, annot=True, fmt="d", cmap="YlGnBu")
plt.show()
```

Include a color bar in the heatmap. Set the range of the color bar from 0 to 600. Center the colormap at the value of passengers in June, 1954.
```python
sns.heatmap(flights, cbar=True, vmin=0, vmax=600, center=flights.loc["Jun", 1954])
plt.show()
```

Add a thin line of width 0.5 between each cell. Create a mask where the number of passengers is less than 200 and apply it to the heatmap.
```python
mask = flights < 200
sns.heatmap(flights, mask=mask, linewidth=0.5)
plt.show()
```

Finally, change the color map to 'coolwarm' and remove the color bar for a cleaner visual.
```python
sns.heatmap(flights, cmap='coolwarm', cbar=False)
plt.show()
```