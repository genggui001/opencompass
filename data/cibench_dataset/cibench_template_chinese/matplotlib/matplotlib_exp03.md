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

文件路径： `data/matplotlib_dataset03.csv`


从文件路径加载数据集到pandas DataFrame中。显示列名和DataFrame的前5行。

```python
import pandas as pd

path = "data/matplotlib_dataset03.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个关于Culmen Length (mm)的线图，使用figsize=(10,6), color='blue'。
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['Culmen Length (mm)'], color='blue')
plt.title("Line plot of Culmen Length (mm)")
plt.xlabel("Penguins Index")
plt.ylabel("Culmen Length (mm)")
plt.show()
```

创建一个关于Flipper Length (mm)的直方图，使用figsize=(10,6), bins=30, color='green', alpha=0.7。


```python
plt.figure(figsize=(10,6))
plt.hist(df['Flipper Length (mm)'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of Flipper Length (mm)")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.show()
```

绘制Flipper Length (mm)和Body Mass (g)列之间关系的散点图。

```python
plt.scatter(df['Flipper Length (mm)'], df['Body Mass (g)'])
plt.title('Relationship between Flipper Length (mm) and Body Mass (g)')
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
```

创建一个关于"Species"值的饼图，使用figsize=(8,8)。

```python
pie_data = df['Species'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of Species")
plt.show()
```

按Species分组，并使用堆叠条形图可视化每种Specie的Flipper Length (mm)和Body Mass (g)内容。

```python

grouped_data = df.groupby('Species')[['Flipper Length (mm)', 'Body Mass (g)']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('Flipper Length (mm) and Body Mass (g) by Specie')
plt.xlabel('Specie')
plt.ylabel('Average Content')
plt.show()
```

绘制DataFrame的所有数值列之间的相关性热图。

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