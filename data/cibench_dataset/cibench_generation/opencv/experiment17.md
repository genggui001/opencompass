---
jupyter:
  title: Use MobileNetSSD to perform object detection
  module: opencv
  dataset: lena.png, MobileNetSSD_deploy.prototxt, MobileNetSSD_deploy.caffemodel
  difficulty: Middle
  idx: 17
  num_steps: 6
  step_types:
    - exec
    - exec
    - text
    - num
    - exec
    - vis
  modules: 
    - opencv
    - opencv 
    - numpy
    - none
    - numpy
    - opencv & matplotlib 
---

File Path: 'data/lena.png', 'data/MobileNetSSD_deploy.prototxt', 'data/MobileNetSSD_deploy.caffemodel'

Load the pre-trained MobileNet SSD model from your local directory. The model is stored in two files: a .prototxt file and a .caffemodel file. Load the image from path.
```python
import cv2
import matplotlib.pyplot as plt
net = cv2.dnn.readNetFromCaffe('data/MobileNetSSD_deploy.prototxt', 'data/MobileNetSSD_deploy.caffemodel')
image = cv2.imread('data/lena.png')
```

Preprocess the loaded image to ensure it's in the correct format for the model. This involves resizing the image to 300x300 pixels (the input size expected by the model), scaling the pixel values by a factor of 0.007843 (to normalize them), subtracting 127.5 from each pixel value (the mean value expected by the model), and swapping the red and blue channels (as the model expects images in RGB format, not BGR). Set the preprocessed image blob as the input to the model. Perform a forward pass through the model. Get the detection results.
```python
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()
```

Iterate over each detection. For each detection, extract the confidence. Ignore any detections with a confidence less than 0.2, and print the index with valid confidence.
```python
import numpy as np
for i in np.arange(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.2:
        print(i)
```

Extract the coordinates of the bounding box for the detection. The coordinates are given as a percentage of the image's width and height, so multiply them by the actual width and height of the image to get the coordinates in pixels. Then, convert the coordinates to integers.
```python
box = detections[0, 0, 0, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
(startX, startY, endX, endY) = box.astype("int")
```

Draw the bounding box on the image,. Also, draw a label showing the confidence of the detection,. The label and bounding box are both drawn in green. Finally, display the image with the bounding boxes and labels drawn on it. As before, convert the color of the image from BGR to RGB before displaying it.
```python
label = "{}: {:.2f}%".format('object', detections[0, 0, 0, 2] * 100)
cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
y = startY - 15 if startY - 15 > 15 else startY + 15
cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
```
