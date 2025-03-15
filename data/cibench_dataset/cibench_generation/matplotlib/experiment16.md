---
jupyter:
  title: Analyzing Shampoo Sales Data Over Time
  module: matplotlib
  dataset: https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv
  difficulty: MIDDLE
  idx: 16
  num_steps: 5
  step_types:
    - text
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

File Path: "data/matplotlib_dataset16_shampoo.csv".

Load the shampoo sales dataset from the provided URL. We specify the 'Month' column for date parsing and set it as the index for our dataframe.Display the first 5 rows of the dataset.
```python
url = "data/matplotlib_dataset16_shampoo.csv"
import pandas as pd
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')
data.head()
```

Create a line plot of the sales data. We are setting the 'Time' on the x-axis and 'Sales' on the y-axis. We will also include a title for our plot and add a grid.
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(data)
plt.title('Shampoo Sales Over Time')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
```

Enhance the visualization by changing the line color to red.Add markers to the line plot to indicate the individual data points.
```python
plt.figure(figsize=(10,6))
plt.plot(data, marker='o', color='red')
plt.title('Shampoo Sales Over Time')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
```

Change the line style to dashed and add a legend.
```python
plt.figure(figsize=(10,6))
plt.plot(data, marker='o', linestyle='--', color='red')
plt.title('Shampoo Sales Over Time')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
```

Compute the moving average of sales over a window of 6 months. Plot the original sales data and its moving average on the same plot.
```python
data['MA'] = data['Sales'].rolling(window=6).mean()
plt.figure(figsize=(10,6))
plt.plot(data['Sales'], marker='o', linestyle='--', color='red', label='Sales')
plt.plot(data['MA'], marker='o', linestyle='--', color='blue', label='Moving Average')
plt.title('Shampoo Sales Over Time')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
```