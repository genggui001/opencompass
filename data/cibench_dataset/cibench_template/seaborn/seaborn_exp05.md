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

File Path: "data/seaborn_dataset05.csv"

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/seaborn_dataset05.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a scatter plot for 'radius_mean' against 'texture_mean', using color = "blue".
```python
import seaborn as sns
sns.scatterplot(data=df, x="radius_mean", y="texture_mean", color="blue").set(title="Radius Mean vs Texture Mean", xlabel="Radius Mean", ylabel="Texture Mean")
```

Generate a joint plot for 'area_mean' and 'smoothness_mean', using height = 6, color = "green".
```python
sns.jointplot(data=df, x="area_mean", y="smoothness_mean", color="green", height=6).set_axis_labels("Area Mean", "Smoothness Mean").fig.suptitle("Area Mean vs Smoothness Mean")
```

Generate a pair plot for the first five numerical columns, using color = "pastel".
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
df_num = df_num.iloc[:, 0:5]
sns.pairplot(df_num, palette="pastel").fig.suptitle("Cancer Dataset Pairplot")
```

Create a scatterplot of concavity_worst and concave points_worst that colors points based on the 'diagnosis' column, using color ="bright".

```python
sns.scatterplot(data=df, x="concavity_worst", y="concave points_worst", hue="diagnosis", palette="bright").set(title="Diagnosis-based Scatterplot", xlabel="Concavity Worst", ylabel="Concave Points Worst")
```

Create a scatterplot with a regression line to visualize the relationship between 'area_mean' and 'perimeter_mean', using color = "plum".
```python
sns.regplot(data=df, x="area_mean", y="perimeter_mean", color="plum").set(title="Area Mean vs Perimeter Mean", xlabel="Area Mean", ylabel="Perimeter Mean")
```