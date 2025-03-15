---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: user data & movie rating data
  difficulty: Easy
  module: pandas
  idx: 10
  num_steps: 4
  step_types:
    - exec
    - text
    - text
    - vis
  modules:
    - pandas
    - pandas
    - pandas
    - pandas&matplotlib
---

File Path: `data/users.csv`, `data/ratings.csv`

Load the first dataset, which contains user data. Load the second dataset, which contains movie rating data.
```python
import pandas as pd

path1 = "data/users.csv"
users = pd.read_csv(path1)
path2 = "data/ratings.csv"
ratings = pd.read_csv(path2)
```

Merge the two datasets on the 'user_id' column. View the first five rows of this merged DataFrame
```python
merged = pd.merge(users, ratings, on='user_id')
merged.head()
```

Group the merged dataset by the 'occupation' column and compute the mean of the 'rating' column for each group. Display the occupation with the third lowest rating.
```python
grouped = merged.groupby('occupation')['rating'].mean()
sorted_df = grouped.sort_values(ascending=False)
sorted_df.index[-3]
```

Visualize the average ratings by occupation using a bar chart. Set the figure size to (10,6), the title to 'Average Ratings by Occupation', the x-label to 'Occupation', and the y-label to 'Average Rating'.
```python
import matplotlib.pyplot as plt

grouped.plot(kind='bar', figsize=(10,6))
plt.title('Average Ratings by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Average Rating')
plt.show()
```
