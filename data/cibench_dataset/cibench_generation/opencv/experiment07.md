---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 7
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib & numpy
    - opencv & matplotlib & numpy
---

File Path: 'data/lena.png'. 

Load the image from path.
```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('data/lena.png')
```

Convert the loaded RGB image to grayscale and display the grayscale image with a kernel size of (5,5) and sigma value of 0 which means that sigma is computed from kernel size.
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
plt.imshow(blur, cmap='gray')
plt.show()
```

Apply a binary threshold to the blurred image. The threshold value will be 127, the maximum value will be 255 and the type of thresholding is binary. Identify the contours in the thresholded image. Draw the identified contours on the original image. The color of the contours will be green (0,255,0).
```python
ret,thresh1 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = cv2.drawContours(img, contours, -1, (0,255,0), 3)
plt.imshow(cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB))
plt.show()
```

Prepare a marker image of the same size as the original image filled with zeroes. Set the marker values for the regions of interest to 255 which represent all contour regions. Display the segmented image using matplotlib where the regions of interest are in white.
```python
import numpy as np
markers = np.zeros((img.shape[0], img.shape[1]), dtype=np.int32)
for i in range(len(contours)):
    cv2.drawContours(markers, contours, i, (255), -1)
cv2.watershed(img, markers)
plt.imshow(markers, cmap='gray')
plt.show()
```
