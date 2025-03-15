---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 0
  num_steps: 7
  step_types:
    - vis
    - num
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - opencv & matplotlib
    - opencv 
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
---

File Path: 'data/lena.png'. 

Read the image from the path and plot it with matplotlib.
```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('data/lena.png')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
```

Get the pixel values of the image at a specific location, say (100, 100). Print the value.
```python
pixel_value = img[100, 100]
print(pixel_value)
```

Convert the color image to grayscale. Display the grayscale image.
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')
plt.show()
```

Apply a binary threshold to the grayscale image. The threshold value is set to 127 and the maximum value is set to 255. Display the thresholded image.
```python
ret,thresh1 = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap='gray')
plt.show()
```

Blur the image with a kernel size of (5,5). Display the blurred image.
```python
blur_img = cv2.blur(img,(5,5))
plt.imshow(blur_img, cmap='gray')
plt.show()
```

Detect the edges in the image. Set the minimum and maximum threshold values to 100 and 200 respectively. Display the image after edge detection.
```python
edges = cv2.Canny(img,100,200)
plt.imshow(edges, cmap='gray')
plt.show()
```

Rotate the image by 90 degrees. The center of rotation is the center of the image, and the scale is 1. Display the rotated image.
```python
rows,cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rotated_img = cv2.warpAffine(img,M,(cols,rows))
plt.imshow(rotated_img, cmap='gray')
plt.show()
```