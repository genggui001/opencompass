---
jupyter:
  title: Visualizing the 'tips' dataset using seaborn boxplots and violin plots.
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 8
  num_steps: 6
  step_types:
    - text
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

Load the 'tips' dataset directly from seaborn's built-in datasets.
```python
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
```

Create a simple vertical boxplot to visualize the distribution of the 'total_bill' column. Set the x parameter to "day", y to "total_bill", hue to "smoker", data to tips, and palette to "Set3".
```python
import matplotlib.pyplot as plt
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="Set3")
plt.show()
```

Create a notched boxplot of 'total_bill' by 'day'. Adjust the order to ["Sun", "Fri", "Sat", "Thur"].
```python
sns.boxplot(x="day", y="total_bill", data=tips, order=["Sun", "Fri", "Sat", "Thur"])
plt.show()
```

Add a swarmplot on top of the boxplot to show the datapoints. Set the color of the swarmplot to ".25".
```python
sns.boxplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")
plt.show()
```

Add a swarmplot to the violinplot to show the individual observations. Set the color to "white" and edgecolor to "gray"
```python
sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
sns.swarmplot(x="day", y="total_bill", data=tips, color="white", edgecolor="gray")
plt.show()
```

Customize the seaborn plot. Add a title to the plot ("Boxplot of total bill by day"), and labels to the x ("Day") and y axes ("Total Bill").
```python
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Boxplot of total bill by day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
```