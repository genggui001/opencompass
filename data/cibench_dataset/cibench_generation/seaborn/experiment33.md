---
jupyter:
  title: Visualize the distribution of data in the 'total_bill' and 'tip' columns of the dataset using rugplots
  module: seaborn
  dataset: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
  difficulty: EASY
  idx: 33
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - pandas
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---

File Path: 'data/seaborn_tips.csv'. 

Load the dataset from the provided path.
```python
import pandas as pd
data = pd.read_csv('data/seaborn_tips.csv')
data.head()
```

Visualize the distribution of the 'total_bill' column by creating a rugplot. Set the height of the markers to 0.2 and the color to red.
```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.rugplot(data['total_bill'], height=0.2, color='red')
plt.show()
```

Create a histogram for the 'total_bill' column using seaborn's histplot function and add the rugplot at the bottom.
```python
sns.histplot(data['total_bill'], kde=False)
sns.rugplot(data['total_bill'])
plt.show()
```

Create rugplots for both the 'total_bill' and 'tip' columns on the same plot, with different colors for each rugplot.
```python
sns.rugplot(data['total_bill'], color='red')
sns.rugplot(data['tip'], color='blue')
plt.show()
```

Add labels to the x and y axes of the rugplot for the 'total_bill' column and add a title to the rugplot, and a legend.
```python
sns.rugplot(data['total_bill'])
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Rugplot of Total Bill')
plt.legend()
plt.show()
```
