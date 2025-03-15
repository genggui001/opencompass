---
jupyter:
  title: FashionMNIST dataset Operations in PyTorch
  dataset: FashionMNIST dataset
  difficulty: Easy
  module: pytorch
  idx: 20
  num_steps: 6
  step_types:
    - vis
    - exec
    - exec
    - vis
    - exec
    - exec
  modules:
    - pytorch&matplotlib
    - pytorch
    - pytorch
    - pytorch&matplotlib
    - pytorch
    - pytorch
---

Dataset Root Path: './data'

Load the FashionMNIST dataset from Torchvision. Set the root directory to dataset root path. Specify that we want the training dataset by setting 'train' to True. Convert the PIL Image or numpy.ndarray to a PyTorch tensor by setting 'transform' to ToTensor(). Display the first image and label from the training dataset. The image is displayed in grayscale as it's a grayscale image. The label is an integer between 0 to 9 representing the type of clothing.

```python
import torch
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt

# 设置数据集下载的根目录为'data'，并指定下载训练集
root = 'data'
train = True

# 将PIL图像或numpy数组转换为PyTorch张量
transform = transforms.Compose([transforms.ToTensor()])

# 加载FashionMNIST数据集
fashion_mnist_train = torchvision.datasets.FashionMNIST(root=root, train=train, transform=transform)

# 显示第一张图像和标签
image, label = fashion_mnist_train[0]
plt.imshow(image.squeeze(), cmap='gray')
plt.title(f'Label: {label}')
plt.show()
```

Create a custom dataset class that inherits from the Dataset class. This custom class will convert the labels to one-hot encoded vectors. The `__getitem__` method fetches an image-label pair from the dataset based on the index and the `__len__` method returns the number of samples in the dataset.

```python
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, dataset):
        self.dataset = dataset

    def __getitem__(self, index):
        image, label = self.dataset[index]
        return image, torch.nn.functional.one_hot(torch.tensor(label), 10)

    def __len__(self):
        return len(self.dataset)
```

Apply the custom dataset to the training data and print the one-hot encoded label of the first sample. Create a DataLoader for the custom dataset with a batch size of 64 and shuffle set to True. This DataLoader divides the dataset into batches of 64 samples each and shuffles them at every epoch.

```python
# 假设你的自定义数据集类名为 CustomDataset，包含了数据和标签
import numpy as np
class CustomDataset(Dataset):
    def __init__(self):
        # 初始化数据集
        self.data = np.random.rand(100, 28, 28)  # 假设有100个28x28的随机数据
        self.labels = np.random.randint(0, 10, size=100)  # 假设有100个随机标签（0到9之间）

    def __getitem__(self, index):
        # 返回数据和标签
        x = self.data[index]
        y = self.labels[index]
        return x, y

    def __len__(self):
        # 返回数据集的大小
        return len(self.data)

# 创建自定义数据集实例
custom_dataset = CustomDataset()

# 将标签转换为独热编码
one_hot_labels = np.eye(10)[custom_dataset.labels]

# 创建DataLoader
batch_size = 64
shuffle = True
data_loader = DataLoader(custom_dataset, batch_size=batch_size, shuffle=shuffle)

# 现在你可以使用data_loader来迭代训练数据集
for batch in data_loader:
    # 在这里执行你的训练循环
    pass

```


Print the shape of the images and labels of the first batch from the DataLoader to verify that the DataLoader is working properly. Display the first 8 images and their corresponding labels from the first batch to ensure that the images and labels are correctly paired.

```python
# 定义转换
transform = transforms.Compose([transforms.ToTensor()])

# 加载FashionMNIST数据集
trainset = torchvision.datasets.FashionMNIST(root='./data', train=True, transform=transform)

# 创建DataLoader
batch_size = 64
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True)

# 获取第一个批次
for images, labels in trainloader:
    # 打印第一个批次的图像和标签的形状
    print("Shape of images in the first batch:", images.shape)
    print("Shape of labels in the first batch:", labels.shape)

    # 显示第一个批次中的前8张图像及其对应的标签
    plt.figure(figsize=(10, 4))
    for i in range(8):
        plt.subplot(2, 4, i+1)
        plt.imshow(images[i].squeeze(), cmap='gray')
        plt.title(f'Label: {labels[i]}')
        plt.axis('off')
    plt.show()

    break  # 仅获取第一个批次
```

Create a DataLoader with 4 workers and measure the time it takes to iterate over the entire dataset. The number of workers refers to the number of subprocesses used for data loading. More workers can potentially decrease the data loading time.

```python
import time

# Define the transformation
transform = transforms.Compose([transforms.ToTensor()])

# Load the FashionMNIST dataset
trainset = torchvision.datasets.FashionMNIST(root='./data', train=True, transform=transform)

# Create DataLoader with 4 workers
batch_size = 64
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=4)

# Measure the time it takes to iterate over the entire dataset
start_time = time.time()
for images, labels in trainloader:
    pass
end_time = time.time()

# Calculate the total time
total_time = end_time - start_time
print(f"Total time to iterate over the entire dataset: {total_time:.2f} seconds")
```

Repeat the previous step, but this time with a single worker. This will help us understand the speed differences when changing the number of workers.

```python
# Define the transformation
transform = transforms.Compose([transforms.ToTensor()])

# Load the FashionMNIST dataset
trainset = torchvision.datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)

# Create DataLoader with 4 workers
batch_size = 64
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=4)

# Measure the time it takes to iterate over the entire dataset
start_time = time.time()
for images, labels in trainloader:
    pass
end_time = time.time()

# Calculate the total time
total_time = end_time - start_time
print(f"Total time to iterate over the entire dataset: {total_time:.2f} seconds")
```