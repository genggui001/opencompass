---
jupyter:
  title: Predicting Boston Housing Prices using Linear Regression in PyTorch
  dataset: Boston Housing Prices
  difficulty: Easy
  module: pytorch
  idx: 46
  num_steps: 6
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
    - vis
  modules:
    - pytorch&pandas&sklearn
    - pytorch&sklearn
    - pytorch
    - pytorch&numpy
    - pytorch
    - pytorch&matplotlib
---

File Path: data/pytorch_gen_dataset03.csv


Load the Boston Housing dataset. Normalize the data using Min-Max Scaling. This step is crucial as it brings all the features to a similar scale.
```python
import pandas as pd
import torch
from sklearn.preprocessing import MinMaxScaler
url = 'data/pytorch_gen_dataset03.csv'
df = pd.read_csv(url)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df.values)
```


Split the normalized data into training and testing sets. The test size is set to be 20% of the total data.
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    scaled_data[:, :-1], 
    scaled_data[:, -1], 
    test_size=0.2, 
    random_state=42
)
```

The numpy arrays are converted into PyTorch tensors as PyTorch models expect the inputs to be tensors.
```python
import numpy as np
X_train = torch.FloatTensor(X_train)
X_test = torch.FloatTensor(X_test)
y_train = torch.FloatTensor(y_train).view(-1, 1)
y_test = torch.FloatTensor(y_test).view(-1, 1)
```


Define a simple linear regression model with 13 inputs (for the 13 features) and 1 output (for the target variable).
```python
class LinearRegressionModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

model = LinearRegressionModel(13, 1)
```


Define the Mean Squared Error (MSE) as the loss function and Stochastic Gradient Descent (SGD) as the optimizer with a learning rate of 0.01. Train the model for 500 epochs.
```python
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for epoch in range(500):
    model.train()
    optimizer.zero_grad()
    y_pred = model(X_train)
    loss = criterion(y_pred, y_train)
    loss.backward()
    optimizer.step()
```


Set the model to evaluation mode and make predictions on the test set. Compute the MSE to evaluate the model's performance. Plot the predicted prices against the actual prices to visualize the model's performance.
```python
import matplotlib.pyplot as plt
model.eval()
y_pred = model(X_test)
test_loss = criterion(y_pred, y_test)
plt.scatter(y_test.detach().numpy(), y_pred.detach().numpy())
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()
```