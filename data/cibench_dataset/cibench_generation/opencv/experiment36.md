---
jupyter:
  title: Classify Iris Data by using the ml.ANN_MLP_create() function of opencv
  module: opencv
  dataset: iris_dataset.csv
  difficulty: Middle
  idx: 36
  num_steps: 5
  step_types:
    - exec
    - exec
    - exec
    - num
    - vis
  modules: 
    - pandas
    - sklearn
    - opencv & numpy & sklearn
    - opencv & numpy & sklearn
    - sklearn & matplotlib & seaborn
---

File Path: 'data/iris_dataset.csv'.

Load the Iris dataset from the path and shuffle the data. Split the data into input and output variables. The input variables are the four features of the flowers, and the output variable is the class of the flowers.
```python
import pandas as pd
dataset = pd.read_csv('data/iris_dataset.csv')
dataset = dataset.sample(frac=1) 
X = dataset.iloc[:,0:4].values
y = dataset.iloc[:,4].values
```

Encode the class labels to integers using LabelBinarizer. This is necessary to perform multiclass classification. Split the data into training and testing sets with a test size of 0.2. This means that 80% of the data will be used for training and 20% for testing.
```python
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
lb = LabelBinarizer()
y = lb.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
```

Create a neural network using OpenCV's ANN_MLP module. The network will have 4 inputs, 3 outputs and two hidden layers each with 10 neurons. The training method is set to backpropagation and the activation function is set to symmetric sigmoid. Normalize the training data and train the neural network using the normalized training data and training labels.
```python
import cv2 as cv
import numpy as np
model = cv.ml.ANN_MLP_create()
layer_sizes = np.int32([4, 10, 10, 3])
model.setLayerSizes(layer_sizes)
model.setTrainMethod(cv.ml.ANN_MLP_BACKPROP)
model.setActivationFunction(cv.ml.ANN_MLP_SIGMOID_SYM, 2, 1)
model.setTermCriteria((cv.TERM_CRITERIA_COUNT, 100, 1e-2))
X_train = cv.normalize(X_train, X_train)
model.train(np.float32(X_train), cv.ml.ROW_SAMPLE, np.float32(y_train))
```

Normalize the testing data and predict the labels using the trained neural network. Calculate the accuracy of the prediction by comparing the predicted labels with the true labels (round to 1 decimal places)
```python
X_test = cv.normalize(X_test, X_test)
ret, resp = model.predict(X_test)
prediction = resp.argmax(axis=-1)
true_labels = y_test.argmax(axis=-1)
accuracy = np.mean(prediction == true_labels)
round(accuracy,1)
```

Generate the confusion matrix of the prediction and plot it for better visualization. The confusion matrix gives a clear view of the prediction performance of the model.
```python
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
cm = confusion_matrix(prediction, true_labels)
plt.figure(figsize=(10,10))
sns.heatmap(cm, annot=True, fmt=".0f", linewidths=.5, square = True, cmap = 'Blues')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Confusion Matrix', size = 15)
plt.show()
```