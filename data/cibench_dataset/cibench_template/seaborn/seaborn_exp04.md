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

File Path: "data/seaborn_dataset04.csv"

Load the dataset from the file path into a pandas DataFrame. Display the column names and the first 5 rows of the DataFrame.
```python
import pandas as pd

path = "data/seaborn_dataset04.csv"
df = pd.read_csv(path)
print(df.columns)
print(df.head(5))
```

Create a scatter plot for 'Glucose' against 'BMI', using color = "blue".
```python
import seaborn as sns
sns.scatterplot(data=df, x="Glucose", y="BMI", color="blue").set(title="Glucose vs BMI", xlabel="Glucose", ylabel="BMI")
```

Generate a joint plot for 'BloodPressure' and 'Age', using height = 6, color = "green".
```python
sns.jointplot(data=df, x="BloodPressure", y="Age", color="green", height=6).set_axis_labels("Blood Pressure", "Age").fig.suptitle("Blood Pressure vs Age")
```

Generate a pair plot for all the numerical columns, using color = "pastel".
```python
# select all the numerical columns
df_num = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(df_num, palette="pastel").fig.suptitle("Diabetes Dataset Pairplot")
```

Generate a violin plot for 'DiabetesPedigreeFunction' based on different outcome, using color = "orange".
```python
sns.violinplot(data=df, x="Outcome", y="DiabetesPedigreeFunction", color="orange").set(title="Violin Plot of 'DiabetesPedigreeFunction'", xlabel="Outcome", ylabel="DiabetesPedigreeFunction")

```
Create a scatterplot of Glucose and Insulin that colors points based on the 'Outcome' column, using color = "bright".
```python
sns.scatterplot(data=df, x="Glucose", y="Insulin", hue="Outcome", palette="bright").set(title="Outcome-based Scatterplot", xlabel="Glucose", ylabel="Insulin")
```

Create a scatterplot with a regression line to visualize the relationship between 'SkinThickness' and 'BMI', using color = "plum".
```python
sns.regplot(data=df, x="SkinThickness", y="BMI", color="plum").set(title="Skin Thickness vs BMI", xlabel="Skin Thickness", ylabel="BMI")
```