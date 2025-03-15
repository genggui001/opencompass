---
jupyter:
  title: classify handwritten digits using the MNIST data set
  dataset: MNIST dataset
  difficulty: Easy
  module: pytorch
  idx: 2
  num_steps: 6
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
    - vis
  modules:
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch & matplotlib
---

Dataset Root Path: './data'

Load and preprocess the MNIST dataset. Apply transformations to the data to normalize the pixel values. Split the data into a training set containing 60,000 examples and a test set containing 10,000 examples. Create data loaders for both the training and test sets with a batch size of 32. Shuffle the training set to ensure that the model gets different order of data in each epoch.

```python
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

train_dataset = datasets.MNIST(root='./data', train=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform)

train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=32, shuffle=False)
```

Define the neural network model. This model will consist of two layers: the first layer will contain 784 neurons (one for each pixel in the 28x28 image) and the second layer will contain 10 neurons (one for each digit from 0 to 9).
```python
import torch.nn as nn
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 500)
        self.fc2 = nn.Linear(500, 10)
    def forward(self, x):
        x = x.view(-1, 784)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = Net()
```

Use the CrossEntropyLoss function from the torch.nn library as the loss function. Use the Stochastic Gradient Descent (SGD) optimizer from the torch.optim library to optimize the model's parameters. Set the learning rate to 0.01 and the momentum to 0.5.
```python
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)
```

Train the model. Repeat this process for a total of two epochs.
```python

def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data.requires_grad = True
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 1000 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.data))

for epoch in range(1):
    train(epoch)
```

Test the model. Evaluate the model using the test set. Compute the total loss and the number of correct predictions, then print the average loss and the accuracy. 
```python
import numpy as np

def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        with torch.no_grad():
            output = model(data)
            test_loss += criterion(output, target).data
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

test()
```

Generate predictions for a batch of test data and visualize the results. Display the first six images from the batch and their corresponding predicted labels.
```python
import matplotlib.pyplot as plt
examples = enumerate(test_loader)
batch_idx, (example_data, example_targets) = next(examples)

with torch.no_grad():
    output = model(example_data)

fig = plt.figure()
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.tight_layout()
    plt.imshow(example_data[i][0], cmap='gray', interpolation='none')
    plt.title("Prediction: {}".format(
      output.data.max(1, keepdim=True)[1][i].item()))
    plt.xticks([])
    plt.yticks([])
plt.show()
```

