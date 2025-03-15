---
jupyter:
  title: Plotting tasks using matplotlib
  dataset: cancer dataset
  difficulty: Middle
  module: matplotlib
  idx: 5
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

File Path: `data/matplotlib_dataset05.csv`

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/matplotlib_dataset05.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a line plot of "mean radius", using figsize=(10,6), color='blue'.
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['mean radius'], color='blue')
plt.title("Line plot of mean radius")
plt.xlabel(" Cancer Index")
plt.ylabel("mean radius")
plt.show()
```

Create a histogram of the mean texture, using figsize=(10,6), bins=30, color='green', alpha=0.7. 

```python
plt.figure(figsize=(10,6))
plt.hist(df['mean texture'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of mean texture")
plt.xlabel("mean texture")
plt.ylabel("Frequency")
plt.show()
```

Draw a scatter graph of the relationship between 'mean area' and 'mean smoothness' columns.

```python
plt.scatter(df['mean area'], df['mean smoothness'])
plt.title('Relationship between mean area and mean smoothness')
plt.xlabel("mean area")
plt.ylabel("mean smoothness")
plt.show()
```

Create a pie chart of the unique values of "diagnosis", using figsize=(8,8).

```python
pie_data = df['diagnosis'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of diagnosis")
plt.show()
```

Group by diagnosis and visualize mean compactness and mean concavity content of each diagnosis using a stacked bar chart.

```python

grouped_data = df.groupby('diagnosis')[['mean compactness', 'mean concavity']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('mean compactness and mean concavity by diagnosis')
plt.xlabel('diagnosis')
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