---
jupyter:
  title: Image classification tasks in tensorflow
  dataset: animal
  difficulty: High
  model: convnet
  module: tensorflow
  idx: 2
  num_steps: 6
  step_types:
    - exec
    - exec
    - exec
    - vis
    - num
    - vis
  modules:
    - tensorflow
    - tensorflow
    - tensorflow
    - matplotlib
    - tensorflow
    - numpy & matplotlib & tensorflow
  
---


File Path : 'data/tensorflow_dataset02'
### Load the flower dataset from {data/tensorflow_dataset02}. There are 8 subfolders in the folder, each containing a different number of images, one subfolder representing a category, and the name of the subfolder is the label. You need to divide the images for each category into training sets and test sets in a ratio of 4:1. Normalize the size of each image to (200,200,3) and normalize the pixel values of each image to between 0 and 1.
```python
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
data_dir = 'data/tensorflow_dataset02'
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
batch_size = 32
target_size = (200, 200)

train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=target_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=target_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)
```

### Construct a convolutional neural network model. The size of the input should be {(200,200,3)} and the size of the output should be {8} which represents the number of image categories.
```python
from tensorflow.keras import layers, models
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(target_size[0], target_size[1], 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(8, activation='softmax'))  
```

### Compile the model. Define Adam as optimizer and SparseCategoricalCrossentropy as loss function. Choose 'accuracy' as the metric to be monitored during training and evaluation. Train the model for {5} epochs.
```python
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_generator, epochs=5, validation_data=validation_generator)
```

### Draw a plot where the accuracy on the training set and the validation set changes with the number of training epochs. Two lines are displayed on one plot with label 'accuracy' and 'val_accuracy'. Set the x-label as 'Epoch' and y-label as 'Accuracy'. Finally display the plot.
```python
import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()
```

### Evaluate the model. Calculate the result of the test loss plus the test accuracy. Print the result (rounded to two decimal places).
```python
test_loss, test_acc = model.evaluate(validation_generator)
result = test_loss + test_acc
round(result,2)
```

### Select a test image (image index = 42) for prediction. Display the image in a plot with the True label and the Predicted label in the title of the plot. The format should be "True label: {true_label}, Predicted label: {predicted_label}"
```python
import numpy as np
from tensorflow.keras.preprocessing import image
img_index = 2

test_img_path = validation_generator.filepaths[img_index]
test_img = image.load_img(test_img_path, target_size=(200, 200))
test_img = image.img_to_array(test_img) / 255.0  # Normalize pixel values to [0, 1]
test_img = np.expand_dims(test_img, axis=0)
true_label = validation_generator.classes[img_index]

predictions = model.predict(test_img)

plt.imshow(test_img[0])
plt.title(f"True label: {true_label}, Predicted label: {np.argmax(predictions)}")
plt.show()
```

