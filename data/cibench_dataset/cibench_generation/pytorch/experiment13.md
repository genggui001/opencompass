---
jupyter:
  title: An Introduction to Tensor Operations in PyTorch
  dataset: None
  difficulty: Easy
  module: pytorch
  idx: 13
  num_steps: 6
  step_types:
    - exec
    - exec
    - vis
    - exec
    - exec
    - vis
  modules:
    - pytorch
    - pytorch
    - pytorch&matplotlib&numpy
    - pytorch
    - pytorch
    - pytorch&matplotlib
---

Dataset Path: './data/hymenoptera_data'


To feed the images into the model, they must be transformed into tensors and normalized. The transforms for the training set include random resizing and flipping to augment the dataset, whereas the validation set only needs to be resized and cropped.
```python
from torchvision import datasets, models, transforms
import torchvision
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}
```

After setting up transformations, load the dataset of bees and ants images, apply the transformations, and prepare the dataloaders, which will feed the images into the model in batches.
```python
import os
import torch
data_dir = './data/hymenoptera_data'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
                  for x in ['train', 'val']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                             shuffle=True, num_workers=4)
              for x in ['train', 'val']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
class_names = image_datasets['train'].classes
```

Use a helper function to display a few images from the training set. Display several images, should contains images of bees or ants.
```python
import numpy as np
import matplotlib.pyplot as plt
def imshow(inp, title=None):
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)

inputs, classes = next(iter(dataloaders['train']))
out = torchvision.utils.make_grid(inputs)
imshow(out, title=[class_names[x] for x in classes])
```

For this experiment, use a pretrained ResNet18 model. Modify its final layer to match the number of classes in your dataset (2: bees and ants). Also, prepare the loss function (criterion), optimizer, and learning rate scheduler.
```python
import torch
import torch.nn as nn
import torch.optim as optim

model_ft = models.resnet18(pretrained=True)
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 2)

criterion = nn.CrossEntropyLoss()

optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)

exp_lr_scheduler = optim.lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)
```

Define a function to train the model. This function will iterate over the training and validation sets for a specified number of epochs, updating the model's weights based on the loss on the training set and checking the model's performance on the validation set.
```python

import time
import copy

def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  
            else:
                model.eval()  

            running_loss = 0.0
            running_corrects = 0

            for inputs, labels in dataloaders[phase]:
                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
            if phase == 'train':
                scheduler.step()

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    model.load_state_dict(best_model_wts)
    return model
```

Train the model using the function you defined earlier with 1 epoch, and print the training time and the best accuracy achieved on the validation set. Define a function to visualize the model's predictions on a few images from the validation set.
```python
model_ft = train_model(model_ft, criterion, optimizer_ft, exp_lr_scheduler,
                       num_epochs=1)
model_ft.eval()

num_images=6
was_training = model_ft.training
model_ft.eval()
images_so_far = 0

image_list = []
class_list = []
with torch.no_grad():
    for i, (inputs, labels) in enumerate(dataloaders['val']):
        outputs = model_ft(inputs)
        _, preds = torch.max(outputs, 1)

        for j in range(inputs.size()[0]):
            images_so_far += 1
            image_list.append(inputs.cpu().data[j])
            class_list.append(class_names[preds[j]])

            if images_so_far == num_images:
                model_ft.train(mode=was_training)
                break
        if images_so_far == num_images:
            break

image_list = torch.stack(image_list)
out = torchvision.utils.make_grid(image_list)
imshow(out, title=class_list)
```
