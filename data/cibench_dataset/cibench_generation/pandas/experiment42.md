---
jupyter:
  title: Data set preprocessing using pandas in Python
  dataset: iris Dataset
  difficulty: Easy
  module: pandas
  idx: 42
  num_steps: 5
  step_types:
    - exec
    - exec
    - exec
    - exec
    - num
  modules:
    - pandas
    - pandas
    - pandas&sklearn
    - pandas&sklearn
    - pandas&sklearn
---

File Path: `data/iris.csv`


Load the Iris dataset from the provided path, ensuring that the dataset does not include a header. Add meaningful column names to the dataset. The column names should be 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', and 'class'. Display the first five rows of the dataset.
```python
import pandas as pd
data = pd.read_csv('data/iris.csv')
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data.head()
```


Transform the 'class' column into numerical values. Split the dataset into independent variables (x) and the dependent variable (y). The dependent variable is the 'class' column.
```python
data['class'] = data['class'].astype('category').cat.codes
x = data.drop('class', axis=1)
y = data['class']
```


Standardize the independent variables so that they have a mean of 0 and a standard deviation of 1. This step is necessary because different features may have different scales. Split the data into a training set and a testing set. Use 70% of the data for training and 30% for testing. Set the random_state to 1 for reproducibility.
```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

scaler = StandardScaler()
x = pd.DataFrame(scaler.fit_transform(x), columns=x.columns)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
```


Train a logistic regression model on the training data.
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train, y_train)
```

Evaluate the performance of the model on the testing data. Print the accuracy score. Create a confusion matrix to see how well the model performed in classifying the iris species. Display the accuracy and keep to 2 decimal places.
```python
from sklearn.metrics import confusion_matrix

score = model.score(x_test, y_test)

y_pred = model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)

score.round(2)
```
