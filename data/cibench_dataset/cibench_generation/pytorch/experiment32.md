---
jupyter:
  title: Training LSTM models to predict stock opening prices from CSV dataset
  dataset: IMDB Movie Reviews
  difficulty: Easy
  module: pytorch
  idx: 32
  num_steps: 8
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
    - exec
    - exec
    - exec
  modules:
    - pandas&numpy&pandas
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch
---

File Path: data/pytorch_gen_dataset02.csv

Load the dataset from the provided URL. Then, display the first few rows of the data using the head function to understand the structure of the data.
```python
import numpy as np
import pandas as pd
url = 'data/pytorch_gen_dataset02.csv'
data = pd.read_csv(url)
data.head()
```

Extract the 'Open' column from the dataframe. The 'Open' column represents the opening price of the stocks which is the target variable for our model. Normalize the extracted data using numpy's linalg.norm function. This is done to bring all the values in the data to a common scale without distorting the differences in the ranges of values.
```python
open = data['Open'].values
open = open / np.linalg.norm(open)
```

Split the data into 80% for training and 20% for testing. The training data is used to train the model while the test data is used to evaluate the performance of the model.
```python
train_size = int(len(open) * 0.8)
train_data = open[:train_size]
test_data = open[train_size:]
```

Reshape the training and testing data into the format `[batch, sequence, feature]`. This format is required for feeding the data into the LSTM model.
```python
train_data = train_data.reshape(-1, 1, 1)
test_data = test_data.reshape(-1, 1, 1)
```

Convert the training and testing data into PyTorch tensors using the Tensor function. Tensors are a type of data structure used in neural networks.
```python
import torch
train_data = torch.Tensor(train_data)
test_data = torch.Tensor(test_data)
```

Define an LSTM model with an input size of 1, hidden layer size of 100, and output size of 1. LSTM (Long Short Term Memory) is a type of recurrent neural network used in deep learning because it can model sequence data.
```python
import torch.nn as nn
class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

    def forward(self, input_seq):
        lstm_out, _ = self.lstm(input_seq.view(len(input_seq) ,1, -1))
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]
```

Train the model for 150 epochs with a learning rate of 0.001 using the Adam optimizer and MSELoss as the loss function. An epoch is an entire run through the training data, the learning rate determines how fast or slow we will move towards the optimal weights, the optimizer is the algorithm used to update the weights and the loss function is used to measure the model's performance.
```python
model = LSTM()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for i in range(150):
    model.zero_grad()
    output = model(train_data)
    loss = loss_function(output, train_data)
    loss.backward()
    optimizer.step()
```

Set the model to evaluation mode and predict the test data. Then, calculate the final loss value using the MSELoss function.
```python
import matplotlib.pyplot as plt
model.eval()
test_outputs = model(test_data)
loss = loss_function(test_outputs, test_data)
print(loss.item())
```