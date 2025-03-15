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

文件路径： `data/matplotlib_dataset02.csv`

从文件路径加载数据集到pandas DataFrame中，用分号分隔。显示列名和DataFrame的前5行。

```python
import pandas as pd

path = "data/matplotlib_dataset02.csv"
df = pd.read_csv(path, sep=';')
print(df.columns)
print(df.head(5))
```

创建一个关于fixed acidity的线图，使用figsize=(10,6), color='blue'。
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['fixed acidity'], color='blue')
plt.title("Line plot of Fixed Acidity")
plt.xlabel("Wine Index")
plt.ylabel("Fixed Acidity")
plt.show()
```

创建一个关于alcohol的直方图，使用figsize=(10,6), bins=30, color='green', alpha=0.7。

```python
plt.figure(figsize=(10,6))
plt.hist(df['alcohol'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of Alcohol Content")
plt.xlabel("Alcohol Content")
plt.ylabel("Frequency")
plt.show()
```

绘制pH和alcohol列之间关系的散点图。


```python
plt.scatter(df['pH'], df['alcohol'])
plt.title('Relationship between pH and Alcohol')
plt.xlabel('pH')
plt.ylabel('Alcohol')
plt.show()
```

创建一个关于"quality"值的饼图，使用figsize=(8,8)。

```python
pie_data = df['quality'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of Wine Quality")
plt.show()
```

按质量分组，并使用堆叠条形图可视化每种质量的fixed acidity和alcohol content。

```python

grouped_data = df.groupby('quality')[['fixed acidity', 'alcohol']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('Fixed Acidity and Alcohol Content by Quality')
plt.xlabel('Quality')
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