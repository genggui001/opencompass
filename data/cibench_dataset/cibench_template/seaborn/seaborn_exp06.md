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

File Path: "data/seaborn_dataset06.csv"

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/seaborn_dataset06.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a scatter plot for 'rm' against 'medv', using color = "blue".
```python
import seaborn as sns
sns.scatterplot(data=df, x="rm", y="medv", color="blue").set(title="Rooms vs Median Value", xlabel="Average Number of Rooms", ylabel="Median Value")
```

Generate a joint plot for 'age' and 'tax', using height = 6, color = "green".
```python
sns.jointplot(data=df, x="age", y="tax", color="green", height=6).set_axis_labels("Age of Property", "Tax Rate").fig.suptitle("Age vs Tax")
```

Generate a pair plot for all the numerical columns, using color = "pastel".
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("boston house dataset Pairplot")
```

Generate a violin plot for 'lstat' based on different chas, using color = "orange".
```python
sns.violinplot(data=df, x="chas", y="lstat", color="orange").set(title="Violin Plot of lstat", xlabel="chas", ylabel="lstat")

```
Create a scatterplot of nox and medv that colors points based on the 'chas' column, using color = "bright".
```python
sns.scatterplot(data=df, x="nox", y="medv", hue="chas", palette="bright").set(title="chas-based Scatterplot", xlabel="nox", ylabel="medv")
```

Create a scatterplot with a regression line to visualize the relationship between 'b' and 'medv', using color = "plum".
```python
sns.regplot(data=df, x="b", y="medv", color="plum").set(title="Proportion of Blacks vs Median Value", xlabel="Proportion of Blacks by Town", ylabel="Median Value")
```