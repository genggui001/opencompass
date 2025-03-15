---
jupyter:
  title: Predicting Daily Minimum Temperatures using LSTM
  dataset: minimum daily temperatures dataset
  difficulty: Easy
  module: pytorch
  idx: 16
  num_steps: 6
  step_types:
    - vis
    - exec
    - exec
    - exec
    - exec
    - vis 
  modules:
    - pytorch&matplotlib&pandas
    - pytorch&numpy
    - pytorch
    - pytorch
    - pytorch
    - pytorch&matplotlib
---

File Path: data/pytorch_gen_dataset01.csv

Load the dataset using pandas. Visualize the temperature data. Time is on the x-axis and Temperature is on the y-axis.
```python
import pandas as pd
import matplotlib.pyplot as plt

url = 'data/pytorch_gen_dataset01.csv'
data = pd.read_csv(url)
plt.figure(figsize=(12,4))
plt.title('Temperature over Time')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.plot(data['Temp'])
plt.show()
```


Normalize the temperature data. Create sequences of 10 days of temperature data, and use the 11th day as the target.

```python
from sklearn.preprocessing import MinMaxScaler
import numpy as np
scaler = MinMaxScaler(feature_range=(-1, 1))
data_normalized = scaler.fit_transform(data['Temp'].values.reshape(-1,1))
def create_sequences(data, seq_length):
    xs = []
    ys = []
    for i in range(len(data)-seq_length-1):
        x = data[i:(i+seq_length)]
        y = data[i+seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)
seq_length = 10
X, y = create_sequences(data_normalized, seq_length)
```


Split the data into training and test sets. The training set contains 67% of the data and the test set contains the remaining 33%.

```python
import torch
train_size = int(len(y) * 0.67)
test_size = len(y) - train_size
dataX = torch.Tensor(np.array(X))
dataY = torch.Tensor(np.array(y))
trainX = torch.Tensor(np.array(X[0:train_size]))
trainY = torch.Tensor(np.array(y[0:train_size]))
testX = torch.Tensor(np.array(X[train_size:len(X)]))
testY = torch.Tensor(np.array(y[train_size:len(y)]))
```

Define a LSTM model with 1 layer, 64 neurons, and a fully connected output layer. Define the prameters for the model.

```python
import torch.nn as nn

class LSTM(nn.Module):
    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(LSTM, self).__init__()
        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.seq_length = seq_length
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size,
                            num_layers=num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
    def forward(self, x):
        h_0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c_0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        out, _ = self.lstm(x, (h_0, c_0))
        out = self.fc(out[:, -1, :])
        return out
input_size = 1
hidden_size = 2
num_layers = 1
num_classes = 1
lstm = LSTM(num_classes, input_size, hidden_size, num_layers)
```

Train the model for 200 epochs with a learning rate of 0.01. Use Mean Squared Error (MSE) as the loss function and Adam as the optimizer.

```python
num_epochs = 200
learning_rate = 0.01
criterion = torch.nn.MSELoss()    # mean-squared error for regression
optimizer = torch.optim.Adam(lstm.parameters(), lr=learning_rate)
for epoch in range(num_epochs):
    outputs = lstm(trainX)
    optimizer.zero_grad()
    loss = criterion(outputs, trainY)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
      print("Epoch: %d, loss: %1.5f" % (epoch, loss.item()))
```

Test the model by predicting the temperature for the entire dataset and visualize the predicted values and actual values on the same plot.

```python
import matplotlib.pyplot as plt

lstm.eval()
train_predict = lstm(dataX)
data_predict = train_predict.data.numpy()
dataY_plot = dataY.data.numpy()
data_predict = scaler.inverse_transform(data_predict)
dataY_plot = scaler.inverse_transform(dataY_plot)
plt.figure(figsize=(10,6)) 
plt.axvline(x=train_size, c='r', linestyle='--') 
plt.plot(dataY_plot)
plt.plot(data_predict)
plt.suptitle('Time-Series Prediction')
plt.show()
```

