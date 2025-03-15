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

文件路径： `data/matplotlib_dataset05.csv`

从文件路径加载数据集到pandas DataFrame中。显示列名和DataFrame的前5行。
```python
import pandas as pd

path = "data/matplotlib_dataset05.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个关于"mean radius"的线图，使用figsize=(10,6), color='blue'。
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['mean radius'], color='blue')
plt.title("Line plot of mean radius")
plt.xlabel(" Cancer Index")
plt.ylabel("mean radius")
plt.show()
```

创建一个关于mean texture的直方图，使用figsize=(10,6), bins=30, color='green', alpha=0.7。

```python
plt.figure(figsize=(10,6))
plt.hist(df['mean texture'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of mean texture")
plt.xlabel("mean texture")
plt.ylabel("Frequency")
plt.show()
```

绘制'mean area'和'mean smoothness'列之间关系的散点图。

```python
plt.scatter(df['mean area'], df['mean smoothness'])
plt.title('Relationship between mean area and mean smoothness')
plt.xlabel("mean area")
plt.ylabel("mean smoothness")
plt.show()
```

创建一个关于"diagnosis"值的饼图，使用figsize=(8,8)。

```python
pie_data = df['diagnosis'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of diagnosis")
plt.show()
```

按diagnosis分组，并使用堆叠条形图可视化每种诊断的mean compactness和mean concavity。

```python

grouped_data = df.groupby('diagnosis')[['mean compactness', 'mean concavity']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('mean compactness and mean concavity by diagnosis')
plt.xlabel('diagnosis')
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