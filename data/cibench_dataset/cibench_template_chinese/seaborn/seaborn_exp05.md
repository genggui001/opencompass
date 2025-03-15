---
jupyter:
  title: Plotting tasks using seaborn
  dataset: cancer dataset
  difficulty: Middle
  module: seaborn
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
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
---

文件路径： "data/seaborn_dataset05.csv"

从文件路径加载数据集到pandas DataFrame中。显示列名和前5行。

```python
import pandas as pd

path = "data/seaborn_dataset05.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个散点图，用radius_mean作为x轴，texture_mean作为y轴，颜色为蓝色。

```python
import seaborn as sns
sns.scatterplot(data=df, x="radius_mean", y="texture_mean", color="blue").set(title="Radius Mean vs Texture Mean", xlabel="Radius Mean", ylabel="Texture Mean")
```

创建一个联合图，用area_mean作为x轴，smoothness_mean作为y轴，颜色为绿色，高度为6。

```python
sns.jointplot(data=df, x="area_mean", y="smoothness_mean", color="green", height=6).set_axis_labels("Area Mean", "Smoothness Mean").fig.suptitle("Area Mean vs Smoothness Mean")
```

对所有的数值列生成一个pair plot，颜色为粉色。
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
df_num = df_num.iloc[:, 0:5]
sns.pairplot(df_num, palette="pastel").fig.suptitle("Cancer Dataset Pairplot")
```

创建一个散点图，用concavity_worst作为x轴，concave points_worst作为y轴，颜色基于'diagnosis'列，颜色为亮色。

```python
sns.scatterplot(data=df, x="concavity_worst", y="concave points_worst", hue="diagnosis", palette="bright").set(title="Diagnosis-based Scatterplot", xlabel="Concavity Worst", ylabel="Concave Points Worst")
```

创建一个散点图以及一个回归线来可视化area_mean和perimeter_mean之间的关系，颜色为梅红色。
```python
sns.regplot(data=df, x="area_mean", y="perimeter_mean", color="plum").set(title="Area Mean vs Perimeter Mean", xlabel="Area Mean", ylabel="Perimeter Mean")
```