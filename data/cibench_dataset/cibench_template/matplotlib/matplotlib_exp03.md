---
jupyter:
  title: Plotting tasks using matplotlib
  dataset: penguins dataset
  difficulty: Middle
  module: matplotlib
  idx: 3
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

File Path: `data/matplotlib_dataset03.csv`

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/matplotlib_dataset03.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a line plot of Culmen Length (mm), using figsize=(10,6), color='blue'.
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['Culmen Length (mm)'], color='blue')
plt.title("Line plot of Culmen Length (mm)")
plt.xlabel("Penguins Index")
plt.ylabel("Culmen Length (mm)")
plt.show()
```

Create a histogram of the Flipper Length (mm), using figsize=(10,6), bins=30, color='green', alpha=0.7. 

```python
plt.figure(figsize=(10,6))
plt.hist(df['Flipper Length (mm)'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of Flipper Length (mm)")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.show()
```

Draw a scatter graph of the relationship between Flipper Length (mm) and Body Mass (g) columns.

```python
plt.scatter(df['Flipper Length (mm)'], df['Body Mass (g)'])
plt.title('Relationship between Flipper Length (mm) and Body Mass (g)')
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
```

Create a pie chart of the unique values of "Species", using figsize=(8,8).

```python
pie_data = df['Species'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of Species")
plt.show()
```

Group by Species and visualize Flipper Length (mm) and Body Mass (g) content of each Specie using a stacked bar chart.

```python

grouped_data = df.groupby('Species')[['Flipper Length (mm)', 'Body Mass (g)']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('Flipper Length (mm) and Body Mass (g) by Specie')
plt.xlabel('Specie')
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