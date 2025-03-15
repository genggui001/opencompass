---
jupyter:
  title: TensorFlow中的图像分类任务
  dataset: flower
  difficulty: 高
  model: convnet
  module: tensorflow
  idx: 1
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

文件路径：'data/tensorflow_dataset01'
### 从{data/tensorflow_dataset01}加载花朵数据集。文件夹中有5个子文件夹，每个子文件夹包含不同数量的图像，一个子文件夹代表一个类别，子文件夹的名称是标签。需要将每个类别的图像按4:1的比例划分为训练集和测试集。将每个图像的大小标准化为(200,200,3)，并将每个图像的像素值标准化为0到1之间。
```python
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
data_dir = 'data/tensorflow_dataset01'
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

### 构建卷积神经网络模型。输入的大小应为{(200,200,3)}，输出的大小应为{5}，表示图像的类别数。
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
model.add(layers.Dense(5, activation='softmax')) 
```

### 编译模型。将Adam作为优化器，CategoricalCrossentropy作为损失函数。在训练和评估过程中选择监视'accuracy'指标。训练模型{5}个epochs。
```python
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
history = model.fit(train_generator, epochs=5, validation_data=validation_generator)
```

### 绘制图表，显示训练集和验证集上的准确性随训练epochs的变化。在一个图表上显示两条线，标签分别为'accuracy'和'val_accuracy'。将x标签设置为'Epoch'，y标签设置为'Accuracy'。最后显示图表。
```python
import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()
```

### 评估模型。将测试损失和测试准确性加和。打印保留两位小数后的结果。
```python
test_loss, test_acc = model.evaluate(validation_generator)
result = test_loss + test_acc
round(result,2)
```

### 选择一个测试图像（图像索引=2）进行预测。在一个图表中显示图像，标题中包含True label和Predicted label。格式应为"True label: {true_label}, Predicted label: {predicted_label}"。
python
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
