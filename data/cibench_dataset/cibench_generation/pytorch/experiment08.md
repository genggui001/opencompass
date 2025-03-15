---
jupyter:
  title: CIFAR-10 dataset in PyTorch
  dataset: CIFAR-10 dataset
  difficulty: Easy
  module: pytorch
  idx: 8
  num_steps: 5
  step_types:
    - exec
    - exec
    - exec
    - exec
    - exec
  modules:
    - pytorch
    - pytorch
    - pytorch
    - pytorch
    - pytorch
---

Dataset Root Path: './data'

Load the CIFAR10 training and test datasets using torchvision. Normalize the images by transforming them to tensors and scaling them to have values between -1 and 1.

```python
import torch  
from torchvision import datasets, transforms  
  
# 定义数据预处理流程  
transform = transforms.Compose([  
    transforms.ToTensor(),  
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # 归一化到[-1,1]  
])  
  
# 加载训练集和测试集  
trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)  
testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)  
  
# 加载数据集时指定batch size和shuffle参数  
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True)  
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False)
```

Define a Convolutional Neural Network with two convolutional layers and two fully connected layers. The first convolutional layer takes 3 input channels (red, green, blue), applies 6 filters of size 5x5, and outputs 6 channels. The second convolutional layer takes these 6 channels as input, applies 16 filters of size 5x5, and outputs 16 channels. The output of the second convolutional layer is flattened and passed through two fully connected layers, and the final output layer has 10 neurons, one for each class in the dataset.

```python
import torch.nn as nn
import torch.nn.functional as F
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
```

Define a Classification Cross-Entropy loss and SGD with momentum for optimization. The learning rate is set to 0.001 and the momentum is set to 0.9.

```python
import torch.optim as optim
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
```

Train the network for 1 epochs. For each batch of 4 images in the training set, the gradients of the network are zeroed, the network outputs are computed, the loss is computed, the gradients are computed using backpropagation, and the network's parameters are updated.

```python
for epoch in range(1):  # 两个epochs的训练  
    running_loss = 0.0  
    for i, data in enumerate(trainloader, 0):  # 遍历每个batch的数据  
        inputs, labels = data  # 获取输入和标签  
        optimizer.zero_grad()  # 清零梯度（因为PyTorch会累积梯度）  
        outputs = net(inputs)  # 前向传播计算输出  
        loss = criterion(outputs, labels)  # 计算损失  
        loss.backward()  # 反向传播计算梯度  
        optimizer.step()  # 更新网络参数（根据梯度下降）  
        running_loss += loss.item()  # 累计损失值，用于打印平均损失值  
    print('Epoch %d loss: %.3f' % (epoch + 1, running_loss / len(trainloader)))
```

Test the network on the test data and print the accuracy. For each batch of 4 images in the test set, the network outputs are computed, and the class with the highest output is predicted. The accuracy is then computed as the ratio of correct predictions to total images.

```python
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))
```

