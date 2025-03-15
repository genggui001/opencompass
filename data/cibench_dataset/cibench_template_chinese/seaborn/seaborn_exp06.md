---
jupyter:
  title: Plotting tasks using seaborn
  dataset: boston house dataset
  difficulty: Middle
  module: seaborn
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
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
---

文件路径： "data/seaborn_dataset06.csv"

从文件路径加载数据集到pandas DataFrame中。显示列名和前5行。
```python
import pandas as pd

path = "data/seaborn_dataset06.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个散点图，用rm作为x轴，medv作为y轴，颜色为蓝色。
```python
import seaborn as sns
sns.scatterplot(data=df, x="rm", y="medv", color="blue").set(title="Rooms vs Median Value", xlabel="Average Number of Rooms", ylabel="Median Value")
```

创建一个联合图，用age作为x轴，tax作为y轴，颜色为绿色，高度为6。
```python
sns.jointplot(data=df, x="age", y="tax", color="green", height=6).set_axis_labels("Age of Property", "Tax Rate").fig.suptitle("Age vs Tax")
```

对所有的数值列生成一个pair plot，颜色为粉色。
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("boston house dataset Pairplot")
```

基于不同的chas生成一个violin plot，颜色为橙色。
```python
sns.violinplot(data=df, x="chas", y="lstat", color="orange").set(title="Violin Plot of lstat", xlabel="chas", ylabel="lstat")

```

创建一个散点图，用nox作为x轴，medv作为y轴，颜色基于'chas'列，颜色为亮色。
```python
sns.scatterplot(data=df, x="nox", y="medv", hue="chas", palette="bright").set(title="chas-based Scatterplot", xlabel="nox", ylabel="medv")
```

创建一个散点图以及一个回归线来可视化b和medv之间的关系，颜色为梅红色。
```python
sns.regplot(data=df, x="b", y="medv", color="plum").set(title="Proportion of Blacks vs Median Value", xlabel="Proportion of Blacks by Town", ylabel="Median Value")
```