---
jupyter:
  title: Analyzing and Visualizing Tips Dataset
  module: matplotlib
  dataset: 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
  difficulty: MIDDLE
  idx: 17
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis  
    - vis
  modules: 
    - pandas
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

File Path: "data/matplotlib_dataset17_tips.csv".

Loading the Dataset and Exploring the Dataset
```python
data_url = 'data/matplotlib_dataset17_tips.csv'
import pandas as pd
data = pd.read_csv(data_url)
data.head()
```

Let's create a scatter plot with the 'total_bill' column on the x-axis and the 'tip' column on the y-axis. Changing the marker style to a square and color to red and set transparency to 0.5.
```python
import matplotlib.pyplot as plt
plt.scatter(data['total_bill'], data['tip'], marker='s', color='red', alpha=0.5)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
```

Markers in the scatter plot can be resized based on the 'size' column in the dataset. We multiply the 'size' column by 10 to make the size difference more discernible in the plot.
```python
plt.scatter(data['total_bill'], data['tip'], marker='s', color='red', alpha=0.5, s=data['size']*10)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
```

Create a histogram of the 'total_bill' column with 20 bins, blue color and black edge color.

```python
plt.hist(data['total_bill'], bins=20, color='blue', edgecolor='black')
plt.title('Histogram of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()
```

Finally, we will generate a bar plot of the average 'total_bill' for each 'day'. The bar plot will show the average total bill for each day of the week. Green color, transparency 0.7.
```python
avg_bill = data.groupby('day')['total_bill'].mean()
plt.bar(avg_bill.index, avg_bill.values, color='green', alpha=0.7)
plt.title('Average Total Bill per Day')
plt.xlabel('Day')
plt.ylabel('Average Total Bill')
plt.show()
```