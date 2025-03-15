---
jupyter:
  title: Classifying Iris Species Using SVM and k-NN
  module: opencv
  dataset: iris-data
  difficulty: Middle
  idx: 19
  num_steps: 5
  step_types:
    - exec
    - exec
    - num
    - vis
    - num
  modules: 
    - sklearn & numpy
    - opencv 
    - opencv & numpy
    - sklearn & matplotlib 
    - opencv
---

Load the Iris dataset from sklearn.datasets. Split the dataset into training and testing data and set the test size to 0.2 and shuffle False. Convert the training dataset and the labels into the required data types. The training data should be in float32 and the labels should be in int32 data type.
```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, shuffle=False)
X_train = np.array(X_train, dtype=np.float32)
y_train = np.array(y_train, dtype=np.int32)
```

Initialize the SVM classifier. Set the parameters for the SVM classifier. The SVM type should be C_SVC, the kernel should be LINEAR, and the C parameter should be 1. Train the SVM classifier and the training data and labels.
```python
import cv2
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(1)
svm.train(X_train, cv2.ml.ROW_SAMPLE, y_train)
```

Convert the testing data into float32 data type. Use the SVM classifier to predict the classes of the testing data. Calculate the accuracy of the SVM classifier by comparing the predicted classes with the actual classes. Print the accuracy(Keep one decimal places).
```python
X_test = np.array(X_test, dtype=np.float32)
_, y_pred = svm.predict(X_test)
accuracy = (y_test == y_pred).mean()
round(accuracy,1)
```

Plot the confusion matrix using matplotlib and sklearn.metrics.
```python
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10,7))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(len(iris.target_names))
plt.xticks(tick_marks, iris.target_names, rotation=45)
plt.yticks(tick_marks, iris.target_names)
plt.show()
```

Initialize the k-Nearest Neighbors (k-NN) classifier. Train the k-NN classifier and the training data and labels. Use the k-NN classifier to predict the classes of the testing data. Calculate the accuracy of the k-NN classifier by comparing the predicted classes with the actual classes. Print the accuracy(Keep one decimal places).
```python
knn = cv2.ml.KNearest_create()
knn.train(X_train, cv2.ml.ROW_SAMPLE, y_train)
_, y_pred_knn = knn.predict(X_test)
accuracy_knn = (y_test == y_pred_knn).mean()
round(accuracy_knn,1)
```
