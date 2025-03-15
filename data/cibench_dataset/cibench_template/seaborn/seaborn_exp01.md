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

File Path: "data/seaborn_dataset01.csv"

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/seaborn_dataset01.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a scatter plot for sepal length against petal length, using color = "red".
```python
import seaborn as sns
sns.scatterplot(data=df, x="SepalLengthCm", y="PetalLengthCm", color="red").set(title="sepal length against petal length", xlabel="SepalLengthCm", ylabel="PetalLengthCm")
```

Generate a joint plot for sepal width and petal width, using height = 6, color = "green".
```python
sns.jointplot(data=df, x="SepalWidthCm", y="PetalWidthCm", color="green", height=6).set_axis_labels("Sepal Width (cm)", "Petal Width (cm)").fig.suptitle("Sepal vs Petal Width")
```

Generate a pair plot for all the numerical columns, using color = "pastel".
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Iris Dataset Pairplot")
```
Generate a violin plot for petal_width based on different species, using color = "orange".
```python
sns.violinplot(data=df, x="Species", y="PetalWidthCm", color="orange").set(title="Violin Plot of Petal Width", xlabel="Species", ylabel="Petal Width (cm)")

```
Create a scatterplot of sepal length and petal length that colors points based on the 'Species' column, using color = "bright".
```python
sns.scatterplot(data=df, x="SepalLengthCm", y="PetalLengthCm", hue="Species", palette="bright").set(title="Species-based Scatterplot", xlabel="Sepal Length (cm)", ylabel="Petal Length (cm)")
```

Create a scatterplot with a regression line to visualize the relationship between petal_width and sepal_width, using color = "plum".
```python
sns.regplot(data=df, x="PetalWidthCm", y="SepalWidthCm", color="plum").set(title="Petal Width vs Sepal Width", xlabel="Petal Width (cm)", ylabel="Sepal Width (cm)")

```