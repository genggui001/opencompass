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

File Path: "data/seaborn_dataset02.csv"

Load the dataset from the file path into a pandas DataFrame using sep=';'. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/seaborn_dataset02.csv"
df = pd.read_csv(path, sep=';')
print(df.columns)
print(df.head(5))
```

Create a scatter plot for 'alcohol' against 'quality', using color = "red".
```python
import seaborn as sns
sns.scatterplot(data=df, x="alcohol", y="quality", color="red").set(title="Alcohol vs Quality", xlabel="Alcohol", ylabel="Quality")
```

Generate a joint plot for 'fixed acidity' and 'pH', using height = 6, color = "green".
```python
sns.jointplot(data=df, x="fixed acidity", y="pH", color="green", height=6).set_axis_labels("Fixed Acidity", "pH").fig.suptitle("Fixed Acidity vs pH")
```

Generate a pair plot for all the numerical columns, using color = "pastel".
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Wine Quality Dataset Pairplot")
```

Generate a violin plot for 'sulphates' based on different 'quality', using color = "orange".
```python
sns.violinplot(data=df, x="quality", y="sulphates", color="orange").set(title="Violin Plot of Sulphates", xlabel="Quality", ylabel="Sulphates")

```
Create a scatterplot of alcohol and pH that colors points based on the 'quality' column, using color = "bright".
```python
sns.scatterplot(data=df, x="alcohol", y="pH", hue="quality", palette="bright").set(title="Quality-based Scatterplot", xlabel="Alcohol", ylabel="pH")

```
Create a scatterplot with a regression line to visualize the relationship between 'volatile acidity' and 'quality', using color = "plum".
```python
sns.regplot(data=df, x="volatile acidity", y="quality", color="plum").set(title="Volatile Acidity vs Quality", xlabel="Volatile Acidity", ylabel="Quality")

```