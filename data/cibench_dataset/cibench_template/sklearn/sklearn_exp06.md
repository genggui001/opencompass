---
jupyter:
  title: Sklearn classification tasks
  dataset: MonthlyDeaths dataset
  difficulty: Middle
  module: Sklearn
  idx: 6
  num_steps: 7
  step_types:
    - exec
    - exec
    - vis
    - exec
    - vis
    - num
    - vis
  modules:
    - pandas
    - sklearn
    - sklearn & matplotlib
    - sklearn
    - sklearn & matplotlib
    - sklearn
    - sklearn & matplotlib
---

File Path: `data/sklearn_dataset06.csv`

### Load the dataset from the file path into a pandas DataFrame. Display the column names.

```python
import pandas as pd
df = pd.read_csv("data/sklearn_dataset06.csv", encoding='gbk')
df.columns
```

### Split the data into features and target "Year", conduct label encoder towards y label and any other non-numeric columns, then into training and testing sets with test size being 0.2.
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

X = df.drop(columns=['Year'], axis=1)
y = df['Year']
y = LabelEncoder().fit_transform(y)
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Create a SimpleImputer object, populate NaN values in the dataframe with the mean, and fit transformations on X_train and X_test. First perform dimensionality reduction using "PCA" on the feature data ，then display different categories of data in three dimensions.
```python
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

Dimensionality_Reduction = "PCA"
Plot_Title = "PCA of MonthlyDeaths Dataset"

imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.fit_transform(X_test)
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_train)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=LabelEncoder().fit_transform(y_train))
ax.set_title(Plot_Title)
plt.show()
```

### Establish a MLP classifaction model, using optimizer "Adam" and activation function "relu". Then conduct model training for 200 epochs.

```python
from sklearn.neural_network import MLPClassifier

Model_Name = "MLPClassifier"
Optimizer = "adam"
Activation_Function = "relu"

model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=200, activation=Activation_Function, solver=Optimizer, random_state=42)
model.fit(X_train, y_train)
```

### Draw a loss curve with epoch as the horizontal axis and loss as the vertical axis.

```python
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

plt.figure(figsize=(10,6))
plt.plot(model.loss_curve_)
plt.title("Loss Curve")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()
```

### Make predictions on the test set, give the confusion matrix, and count the prediction accuracy, precision, recall, and F1 score of each category. Finally, display the accuracy of the model on the test set (rounded to two decimal places).

```python
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

y_pred = model.predict(X_test)
y_true = y_test

confusion = confusion_matrix(y_true, y_pred)
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average=None)
recall = recall_score(y_true, y_pred, average=None)
f1 = f1_score(y_true, y_pred, average=None)

round(accuracy, 2)
```

### Visualize predictive data with 3D plots.

```python
predictions = model.predict(X_test)
X_pca_test = pca.transform(X_test)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca_test[:, 0], X_pca_test[:, 1], X_pca_test[:, 2], c=LabelEncoder().fit_transform(predictions))
ax.set_title(Plot_Title)
plt.show()
```