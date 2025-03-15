---
jupyter:
  title: Analyzing Titanic Passenger Data
  module: seaborn
  dataset: none
  difficulty: EASY
  idx: 4
  num_steps: 4
  step_types:
    - vis
    - vis
    - vis
    - vis
  modules: 
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---

Load the Titanic dataset from seaborn. Create a bar plot visualizing the survival rate against the sex of the passengers. Adding the 'class' column as an additional dimension
```python
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
sns.barplot(x='sex', y='survived', hue='class', data=df)
plt.show()
```

Modify the color of the bars to blue using the 'palette' parameter. Alter the order of bars to display 'female' before 'male'.
```python
sns.barplot(x='sex', y='survived', hue='class', data=df, palette='Blues', order=['female', 'male'])
plt.show()
```

Decrease the size of the confidence intervals in the bar plot to 68% by. Add caps to the error bars to 0.1.
```python
sns.barplot(x='sex', y='survived', hue='class', data=df, palette='Blues', order=['female', 'male'], ci=68, capsize=0.1)
plt.show()
```

Add a title "Survival by Gender and Class", and labels "Survival Rate" and "Gender" to the x and y axes respectively.
```python
sns.barplot(x='survived', y='sex', hue='class', data=df, palette='Blues', ci=68, capsize=0.1)
plt.title('Survival by Gender and Class')
plt.xlabel('Survival Rate')
plt.ylabel('Gender')
plt.show()
```