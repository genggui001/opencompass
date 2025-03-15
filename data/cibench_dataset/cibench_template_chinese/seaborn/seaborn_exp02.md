---
jupyter:
  title: Plotting tasks using seaborn
  dataset: wine quality dataset
  difficulty: Middle
  module: seaborn
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
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
---

文件路径： "data/seaborn_dataset02.csv"

从文件路径加载数据集到pandas DataFrame中，使用分号分隔。显示列名和前5行。注意用分号分隔。
```python
import pandas as pd

path = "data/seaborn_dataset02.csv"
df = pd.read_csv(path, sep=';')
print(df.columns)
print(df.head(5))
```

创建一个散点图，用alcohol作为x轴，quality作为y轴，颜色为红色。
```python
import seaborn as sns
sns.scatterplot(data=df, x="alcohol", y="quality", color="red").set(title="Alcohol vs Quality", xlabel="Alcohol", ylabel="Quality")
```

创建一个联合图，用fixed acidity作为x轴，pH作为y轴，颜色为绿色，高度为6。
```python
sns.jointplot(data=df, x="fixed acidity", y="pH", color="green", height=6).set_axis_labels("Fixed Acidity", "pH").fig.suptitle("Fixed Acidity vs pH")
```

对所有的数值列生成一个pair plot，颜色为粉色。
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Wine Quality Dataset Pairplot")
```

基于不同的quality生成一个violin plot，颜色为橙色。
```python
sns.violinplot(data=df, x="quality", y="sulphates", color="orange").set(title="Violin Plot of Sulphates", xlabel="Quality", ylabel="Sulphates")

```

创建一个散点图，用alcohol作为x轴，pH作为y轴，颜色基于'quality'列，颜色为亮色。
```python
sns.scatterplot(data=df, x="alcohol", y="pH", hue="quality", palette="bright").set(title="Quality-based Scatterplot", xlabel="Alcohol", ylabel="pH")
```

创建一个散点图以及一个回归线来可视化volatile acidity和quality之间的关系，颜色为梅红色。
```python
sns.regplot(data=df, x="volatile acidity", y="quality", color="plum").set(title="Volatile Acidity vs Quality", xlabel="Volatile Acidity", ylabel="Quality")

```