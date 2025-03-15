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

文件路径： `data/matplotlib_dataset06.csv`

从文件路径加载数据集到pandas DataFrame中。显示列名和DataFrame的前5行。

```python
import pandas as pd

path = "data/matplotlib_dataset06.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个关于MEDV的线图，使用figsize=(10,6), color='blue'。

    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['MEDV'], color='blue')
plt.title("Line plot of MEDV")
plt.xlabel(" House Index")
plt.ylabel("MEDV")
plt.show()
```

创建一个关于CRIM的直方图，使用figsize=(10,6), bins=30, color='green', alpha=0.7。

```python
plt.figure(figsize=(10,6))
plt.hist(df['CRIM'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of CRIM")
plt.xlabel("CRIM")
plt.ylabel("Frequency")
plt.show()
```

绘制NOX和RM列之间关系的散点图。

```python
plt.scatter(df['NOX'], df['RM'])
plt.title('Relationship between NOX and RM')
plt.xlabel("NOX")
plt.ylabel("RM")
plt.show()
```

创建一个关于CHAS值的饼图，使用figsize=(8,8)。

```python
pie_data = df['CHAS'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of CHAS")
plt.show()
```

按CHAS分组，并使用堆叠条形图可视化每个CHAS的RAD和TAX内容。

```python

grouped_data = df.groupby('CHAS')[['RAD', 'TAX']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('RAD and TAX by CHAS')
plt.xlabel('CHAS')
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