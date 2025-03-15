---
jupyter:
  title: Plotting tasks using seaborn
  dataset: diabetes dataset
  difficulty: Middle
  module: seaborn
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
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
    - seaborn
---

文件路径： "data/seaborn_dataset04.csv"

从文件路径加载数据集到pandas DataFrame中。显示列名和前5行。
```python
import pandas as pd

path = "data/seaborn_dataset04.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

创建一个散点图，用Glucose作为x轴，BMI作为y轴，颜色为蓝色。

```python
import seaborn as sns
sns.scatterplot(data=df, x="Glucose", y="BMI", color="blue").set(title="Glucose vs BMI", xlabel="Glucose", ylabel="BMI")
```

创建一个联合图，用BloodPressure作为x轴，Age作为y轴，颜色为绿色，高度为6。
```python
sns.jointplot(data=df, x="BloodPressure", y="Age", color="green", height=6).set_axis_labels("Blood Pressure", "Age").fig.suptitle("Blood Pressure vs Age")
```

对所有的数值列生成一个pair plot，颜色为粉色。
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Diabetes Dataset Pairplot")
```

基于不同的outcome生成一个violin plot，颜色为橙色。
```python
sns.violinplot(data=df, x="Outcome", y="DiabetesPedigreeFunction", color="orange").set(title="Violin Plot of 'DiabetesPedigreeFunction'", xlabel="Outcome", ylabel="DiabetesPedigreeFunction")
```

创建一个散点图，用Glucose作为x轴，Insulin作为y轴，颜色基于'Outcome'列，颜色为亮色。
```python
sns.scatterplot(data=df, x="Glucose", y="Insulin", hue="Outcome", palette="bright").set(title="Outcome-based Scatterplot", xlabel="Glucose", ylabel="Insulin")
```

创建一个散点图以及一个回归线来可视化SkinThickness和BMI之间的关系，颜色为梅红色。
```python
sns.regplot(data=df, x="SkinThickness", y="BMI", color="plum").set(title="Skin Thickness vs BMI", xlabel="Skin Thickness", ylabel="BMI")
```