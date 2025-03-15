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

文件路径： `data/matplotlib_dataset04.csv`

从文件路径加载数据集到pandas DataFrame中。显示列名和DataFrame的前5行。

```python
import pandas as pd

path = "data/matplotlib_dataset04.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个关于age的线图，使用figsize=(10,6), color='blue'。
    
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['age'], color='blue')
plt.title("Line plot of age")
plt.xlabel("Index")
plt.ylabel("age")
plt.show()
```

创建一个关于chol的直方图，使用figsize=(10,6), bins=30, color='green', alpha=0.7。

```python
plt.figure(figsize=(10,6))
plt.hist(df['chol'], bins=30, color='green', alpha=0.7)
plt.title("Histogram of chol")
plt.xlabel("chol")
plt.ylabel("Frequency")
plt.show()
```

绘制"maximum heart rate"和"age"列之间关系的散点图。

```python
plt.scatter(df['maximum heart rate'], df['age'])
plt.title('Relationship between maximum heart rate and age')
plt.xlabel("maximum heart rate")
plt.ylabel("age")
plt.show()
```

创建一个关于"presence of heart disease"值的饼图，使用figsize=(8,8)。

```python
pie_data = df['presence of heart disease'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
plt.title("Pie chart of presence of heart disease")
plt.show()
```

按presence of heart disease分组，并使用堆叠条形图可视化每种presence of heart disease的blood pressure和chol内容。

```python

grouped_data = df.groupby('presence of heart disease')[['blood pressure', 'chol']].mean()

# Creating a stacked bar chart
grouped_data.plot(kind='bar', stacked=True)
plt.title('blood pressure and chol by presence of heart disease')
plt.xlabel('presence of heart disease')
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