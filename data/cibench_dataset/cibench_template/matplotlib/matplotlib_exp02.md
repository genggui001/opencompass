---
jupyter:
  title: Plotting tasks using matplotlib
  dataset: wine quality dataset
  difficulty: Middle
  module: matplotlib
  idx: 2
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

File Path: `data/matplotlib_dataset02.csv`

Load the dataset from the file path into a pandas DataFrame using sep = ";". Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/matplotlib_dataset02.csv"
df = pd.read_csv(path, sep=';')
print(df.columns)
print(df.head(5))
```

Create a line plot of fixed acidity, using figsize=(10,6), color='blue'.
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['fixed acidity'], color='blue')
plt.title("Line plot of Fixed Acidity")
plt.xlabel("Wine Index")
plt.ylabel("Fixed Acidity")
plt.show()
```

Create a histogram of the alcohol, using figsize=(10,6), bins=30, color='green', alpha=0.7. 

```python
plt.figure(figsize=(10,6))
plt.hist(df['alcohol'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of Alcohol Content")
plt.xlabel("Alcohol Content")
plt.ylabel("Frequency")
plt.show()
```

Draw a scatter graph of the relationship between pH and alcohol columns.

```python
plt.scatter(df['pH'], df['alcohol'])
plt.title('Relationship between pH and Alcohol')
plt.xlabel('pH')
plt.ylabel('Alcohol')
plt.show()
```

Create a pie chart of the unique values of "quality", using figsize=(8,8).

```python
pie_data = df['quality'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of Wine Quality")
plt.show()
```

Group by quality and visualize fixed acidity and alcohol content of each quality using a stacked bar chart.

```python

grouped_data = df.groupby('quality')[['fixed acidity', 'alcohol']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('Fixed Acidity and Alcohol Content by Quality')
plt.xlabel('Quality')
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