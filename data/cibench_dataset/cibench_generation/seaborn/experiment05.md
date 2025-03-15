---
jupyter:
  title: Visualizing the Iris Dataset with Histograms using Seaborn and Matplotlib Libraries
  module: seaborn
  dataset: none
  difficulty: EASY/MIDDLE/HARD
  idx: 5
  num_steps: 5
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
    - seaborn & matplotlib
---


Load the Iris dataset using the seaborn library's built-in load_dataset function.Create a basic histogram for the feature 'sepal_length'. Enhance the granularity of the histogram by increasing the number of bins to 30. Change the color of the histogram to red.
```python
import seaborn as sns
iris = sns.load_dataset('iris')
import matplotlib.pyplot as plt
sns.histplot(iris['sepal_length'], bins=30, color='red')
plt.show()
```

Add labels to the x-axis, y-axis, and a title to the histogram for better understanding.
```python
sns.histplot(iris['sepal_length'], bins=30, color='red')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.show()
```

Create a histogram with a Kernel Density Estimate (KDE) line for 'sepal_width'. Modify the style of the KDE line to a dashed line and change the color of the KDE line to green.
```python
sns.histplot(iris['sepal_width'], kde=True, linestyle='--', color='green')
plt.show()
```

Create a histogram for 'sepal_length' for each species in the dataset. Use the 'hue' parameter to differentiate each species.
```python
sns.histplot(data=iris, x='sepal_length', hue='species')
plt.show()
```

Adjust the size of the figure to 10x6. Improve the 2D histogram by adding a legend that specifies the species.
```python
plt.figure(figsize=(10,6))
sns.histplot(data=iris, x='sepal_length', y='sepal_width')
plt.legend(title='Species', loc='upper right', labels=['setosa', 'versicolor', 'virginica'])
plt.show()
```
