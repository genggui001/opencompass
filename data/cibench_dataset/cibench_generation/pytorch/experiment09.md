---
jupyter:
  title: Basic Classification in PyTorch
  dataset: None
  difficulty: Easy
  module: pytorch
  idx: 9
  num_steps: 7
  step_types:
    - exec
    - exec
    - exec
    - exec
    - vis
    - vis
    - exec
  modules:
    - pytorch&numpy
    - pytorch
    - pytorch
    - pytorch
    - pytorch&matplotlib
    - pytorch&matplotlib
    - pytorch
---


Generate a dataset of 1000 samples where each sample has two features. The samples belong to one of the three classes. We will use NumPy's random function for this. We shall set the seed to 42 to ensure reproducibility. We need to convert our data from NumPy arrays to PyTorch tensors.
```python
import torch
import numpy as np
np.random.seed(42)
x = np.random.rand(1000, 2)
y = np.random.randint(0, 3, (1000, 1))

x = torch.from_numpy(x).float()
y = torch.from_numpy(y).long()
```


Define the neural network architecture. We will use a simple neural network with one hidden layer. The input layer will have 2 neurons corresponding to the two features of our data. The hidden layer will have 5 neurons and the output layer will have 3 neurons, corresponding to the three classes of our data.
```python
model = torch.nn.Sequential(
    torch.nn.Linear(2, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 3)
)
```

Define the loss function and optimizer. We will use the Cross Entropy Loss as our loss function and the Adam optimizer with a learning rate of 0.01. Train the neural network model for 500 epochs. Print the loss value every 100 epochs to monitor the training process.
```python
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
for t in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y.squeeze())
    if t % 100 == 0:
        print(t, loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

Test the model with a new data sample. Let's use the sample [0.5, 0.5] for this.
```python
test_x = torch.Tensor([[0.5, 0.5]])
y_test_pred = model(test_x)
predicted_class = y_test_pred.argmax(1)
print(predicted_class)
```

Create a grid to cover the feature space and use the model to predict the class for each point on the grid. This will allow us to visualize the decision boundary of the trained model.
```python
import matplotlib.pyplot as plt
h = 0.02
x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
grid_tensor = torch.from_numpy(np.c_[xx.ravel(), yy.ravel()]).float()
Z = model(grid_tensor)
Z = Z.data.max(1)[1]
Z = Z.numpy().reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
```

Overlay the original data points on the decision boundary plot. Each point will be colored according to its class.
```python
plt.scatter(x[:, 0], x[:, 1], c=y.squeeze(), edgecolors='k', cmap=plt.cm.Spectral)
plt.show()
```

Calculate the accuracy of the model on the training data. The accuracy is the ratio of the number of correct predictions to the total number of predictions.
```python
y_pred = model(x)
predicted_class = y_pred.argmax(1)
correct = (predicted_class == y.squeeze()).sum().item()
accuracy = correct / y.shape[0]
print('Accuracy: ', accuracy)
```