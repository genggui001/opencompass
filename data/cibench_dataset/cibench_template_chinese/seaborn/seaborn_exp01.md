---
jupyter:
  title: Plotting tasks using seaborn
  dataset: iris dataset
  difficulty: Middle
  module: seaborn
  idx: 1
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

文件路径： "data/seaborn_dataset01.csv"

从文件路径加载数据集到pandas DataFrame中。显示列名和前5行。
```python
import pandas as pd

path = "data/seaborn_dataset01.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个散点图，用sepal length作为x轴，petal length作为y轴，颜色为红色。
```python
import seaborn as sns
sns.scatterplot(data=df, x="SepalLengthCm", y="PetalLengthCm", color="red").set(title="sepal length against petal length", xlabel="SepalLengthCm", ylabel="PetalLengthCm")
```

创建一个联合图，用sepal width作为x轴，petal width作为y轴，颜色为绿色，高度为6。
```python
sns.jointplot(data=df, x="SepalWidthCm", y="PetalWidthCm", color="green", height=6).set_axis_labels("Sepal Width (cm)", "Petal Width (cm)").fig.suptitle("Sepal vs Petal Width")
```

对所有的数值列生成一个pair plot，颜色为粉色。

```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Iris Dataset Pairplot")
```

基于不同的species生成一个violin plot，颜色为橙色。
```python
sns.violinplot(data=df, x="Species", y="PetalWidthCm", color="orange").set(title="Violin Plot of Petal Width", xlabel="Species", ylabel="Petal Width (cm)")

```

创建一个散点图，用sepal length作为x轴，petal length作为y轴，颜色基于'Species'列，颜色为亮色。
```python
sns.scatterplot(data=df, x="SepalLengthCm", y="PetalLengthCm", hue="Species", palette="bright").set(title="Species-based Scatterplot", xlabel="Sepal Length (cm)", ylabel="Petal Length (cm)")
```

创建一个散点图以及一个回归线来可视化petal_width和sepal_width之间的关系，颜色为梅红色。
```python
sns.regplot(data=df, x="PetalWidthCm", y="SepalWidthCm", color="plum").set(title="Petal Width vs Sepal Width", xlabel="Petal Width (cm)", ylabel="Sepal Width (cm)")

```