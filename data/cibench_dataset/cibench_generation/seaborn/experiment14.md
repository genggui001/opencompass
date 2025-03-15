---
jupyter:
  title: Visualizing the 'tips' Dataset Using Various Seaborn Palettes
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 14
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - seaborn
    - seaborn
    - seaborn
    - seaborn
---

Load the 'tips' dataset using seaborn's built-in function.
```python
import seaborn as sns
tips = sns.load_dataset("tips")
```

Display the bright palette in seaborn.
```python
import matplotlib.pyplot as plt
light_palette = sns.color_palette("bright")
sns.palplot(light_palette)
plt.show()
```

Display the coolwarm palette in seaborn.
```python
coolwarm_palette = sns.color_palette("coolwarm", 8)
sns.palplot(coolwarm_palette)
plt.show()
```

Now, visualize the 'tips' dataset using the coolwarm palettes, use replot to set 'x' as "total_bill", 'y' as "tip", 'hue' as "day", and 'style' as "time".
```python
sns.set_palette("coolwarm")
sns.relplot(data=tips, x="total_bill", y="tip", hue="day", style="time")
plt.show()
```
