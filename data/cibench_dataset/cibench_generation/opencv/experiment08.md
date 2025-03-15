---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 8
  num_steps: 4
  step_types:
    - exec
    - num
    - vis
  modules: 
    - opencv
    - opencv 
    - opencv & matplotlib
---

File Path: 'data/lena.png', 'data/haarcascade_frontalface_default.xml'.

Load the target image in grayscale mode.
```python
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('data/lena.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Load the pre-trained Haar Cascade classifier for face detection provided by OpenCV. Run the face detection algorithm on the grayscale image. The parameters are set as scaleFactor=1.1, minNeighbors=5, and minSize=(30, 30) to ensure accurate detection. Determine the number of faces detected by the algorithm by finding the length of the faces array. Print this information.
```python
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print(len(faces))
```

Highlight the detected faces in the original image by drawing rectangles around them from the cv2 library. The color of the rectangle is set to blue (255, 0, 0) and its thickness is set to 2. Convert the color scheme of the image with highlighted faces from BGR to RGB. Finally, visualize the original image with the detected faces highlighted. This will show the effectiveness of the face detection algorithm.
```python
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()
```
