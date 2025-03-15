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

File Path: "data/seaborn_dataset03.csv"

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/seaborn_dataset03.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a scatter plot for 'weight' against 'mpg', using color = "blue".
```python
import seaborn as sns
sns.scatterplot(data=df, x="weight", y="mpg", color="blue").set(title="Weight vs MPG", xlabel="Weight", ylabel="MPG")
```

Generate a joint plot for 'horsepower' and 'acceleration', using height = 6, color = "green".
```python
sns.jointplot(data=df, x="horsepower", y="acceleration", color="green", height=6).set_axis_labels("Horsepower", "Acceleration").fig.suptitle("Horsepower vs Acceleration")
```

Generate a pair plot for all the numerical columns, using color = "pastel".
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Auto MPG Dataset Pairplot")
```

Generate a violin plot for model year based on different origin, using color = "orange".
```python
sns.violinplot(data=df, x="origin", y="model year", color="orange").set(title="Violin Plot of model year", xlabel="origin", ylabel="model year")

```
Create a scatterplot of displacement and mpg that colors points based on the 'origin' column, using color = "bright".
```python
sns.scatterplot(data=df, x="displacement", y="mpg", hue="origin", palette="bright").set(title="origin-based Scatterplot", xlabel="Displacement", ylabel="MPG")
```

Create a scatterplot with a regression line to visualize the relationship between 'weight' and 'mpg', using color = "plum".
```python
sns.regplot(data=df, x="weight", y="mpg", color="plum").set(title="Weight vs MPG", xlabel="Weight", ylabel="MPG")

```