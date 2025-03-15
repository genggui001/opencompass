---
jupyter:
  title: Plotting tasks using matplotlib
  dataset: heart dataset
  difficulty: Middle
  module: matplotlib
  idx: 4
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

File Path: `data/matplotlib_dataset04.csv`

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/matplotlib_dataset04.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a line plot of "age", using figsize=(10,6), color='blue'.
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['age'], color='blue')
plt.title("Line plot of age")
plt.xlabel("Index")
plt.ylabel("age")
plt.show()
```

Create a histogram of the chol, using figsize=(10,6), bins=30, color='green', alpha=0.7. 

```python
plt.figure(figsize=(10,6))
plt.hist(df['chol'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of chol")
plt.xlabel("chol")
plt.ylabel("Frequency")
plt.show()
```

Draw a scatter graph of the relationship between "maximum heart rate" and "age" columns.

```python
plt.scatter(df['maximum heart rate'], df['age'])
plt.title('Relationship between maximum heart rate and age')
plt.xlabel("maximum heart rate")
plt.ylabel("age")
plt.show()
```

Create a pie chart of the unique values of "presence of heart disease", using figsize=(8,8).

```python
pie_data = df['presence of heart disease'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of presence of heart disease")
plt.show()
```

Group by presence of heart disease and visualize blood pressure and chol content of each presence of heart disease using a stacked bar chart.

```python

grouped_data = df.groupby('presence of heart disease')[['blood pressure', 'chol']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('blood pressure and chol by presence of heart disease')
plt.xlabel('presence of heart disease')
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