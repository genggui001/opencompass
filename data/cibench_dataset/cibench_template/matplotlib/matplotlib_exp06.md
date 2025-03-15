---
jupyter:
  title: Plotting tasks using matplotlib
  dataset: house price dataset
  difficulty: Middle
  module: matplotlib
  idx: 6
  num_steps: 7
  step_types:
    - exec
    - vis
    - vis
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
    - matplotlib
    - matplotlib
---

File Path: `data/atplotlib_dataset06.csv`

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/matplotlib_dataset06.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a line plot of "MEDV", using figsize=(10,6), color='blue'.
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['MEDV'], color='blue')
plt.title("Line plot of MEDV")
plt.xlabel(" House Index")
plt.ylabel("MEDV")
plt.show()
```

Create a histogram of the CRIM, using figsize=(10,6), bins=30, color='green', alpha=0.7. 

```python
plt.figure(figsize=(10,6))
plt.hist(df['CRIM'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of CRIM")
plt.xlabel("CRIM")
plt.ylabel("Frequency")
plt.show()
```

Draw a scatter graph of the relationship between "NOX" and "RM" columns.

```python
plt.scatter(df['NOX'], df['RM'])
plt.title('Relationship between NOX and RM')
plt.xlabel("NOX")
plt.ylabel("RM")
plt.show()
```

Create a pie chart of the unique values of "CHAS", using figsize=(8,8).

```python
pie_data = df['CHAS'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of CHAS")
plt.show()
```

Group by CHAS and visualize "RAD" and "TAX" content of each CHAS using a stacked bar chart.

```python

grouped_data = df.groupby('CHAS')[['RAD', 'TAX']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('RAD and TAX by CHAS')
plt.xlabel('CHAS')
plt.ylabel('Average Content')
plt.show()
```

Draw a heatmap of the correlation between all the nemerical columns of the DataFrame. 

```python
# Select all the numerical columns
df = df.select_dtypes(include=['float64', 'int64'])
corr = df.corr()
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=90)
plt.yticks(range(len(corr)), corr.columns)
plt.show()
```