---
jupyter:
  title: Plotting tasks using seaborn
  dataset: auto mpg dataset
  difficulty: Middle
  module: seaborn
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
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
---

文件路径： "data/seaborn_dataset03.csv"

从文件路径加载数据集到pandas DataFrame中。显示列名和前5行。
```python
import pandas as pd

path = "data/seaborn_dataset03.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个散点图，用weight作为x轴，mpg作为y轴，颜色为蓝色。
```python
import seaborn as sns
sns.scatterplot(data=df, x="weight", y="mpg", color="blue").set(title="Weight vs MPG", xlabel="Weight", ylabel="MPG")
```

创建一个联合图，用horsepower作为x轴，acceleration作为y轴，颜色为绿色，高度为6。
```python
sns.jointplot(data=df, x="horsepower", y="acceleration", color="green", height=6).set_axis_labels("Horsepower", "Acceleration").fig.suptitle("Horsepower vs Acceleration")
```

对所有的数值列生成一个pair plot，颜色为粉色。
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Auto MPG Dataset Pairplot")
```

基于不同的origin生成一个violin plot，颜色为橙色。
```python
sns.violinplot(data=df, x="origin", y="model year", color="orange").set(title="Violin Plot of model year", xlabel="origin", ylabel="model year")

```

创建一个散点图，用displacement作为x轴，mpg作为y轴，颜色基于'origin'列，颜色为亮色。
```python
sns.scatterplot(data=df, x="displacement", y="mpg", hue="origin", palette="bright").set(title="origin-based Scatterplot", xlabel="Displacement", ylabel="MPG")
```

创建一个散点图以及一个回归线来可视化weight和mpg之间的关系，颜色为梅红色。
```python
sns.regplot(data=df, x="weight", y="mpg", color="plum").set(title="Weight vs MPG", xlabel="Weight", ylabel="MPG")

```