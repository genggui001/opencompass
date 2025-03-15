---
jupyter:
  title: Contour Detection and Analysis using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: Middle
  idx: 21
  num_steps: 8
  step_types:
    - vis
    - vis
    - num
    - num
    - num
    - vis
    - vis
    - vis
  modules:
    - opencv & matplotlib & numpy
    - opencv & matplotlib
    - opencv 
    - opencv  
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
---

File Path: 'data/lena.png'.

Load the image and convert the color scheme of the image from BGR to RGB. Convert the RGB image to grayscale. Apply binary thresholding to the grayscale image with 100 as the threshold value and 255 as the max value. Then, visualize the threshold images.
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('data/lena.png', cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
plt.imshow(threshold, cmap='gray')
plt.show()
```

Find contours in the thresholded image. Use the simple chain approximation method (`cv2.CHAIN_APPROX_SIMPLE`). Draw the 4th contour in the contours list on another copy of the original image. Display this image.
```python
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_specific_contour = cv2.drawContours(image.copy(), contours, 3, (0,255,0), 3)
plt.imshow(image_specific_contour)
plt.show()
```

Calculate the maximum area of the contour and print the result(Keep two decimal places).
```python
area_list = []
for i, cnt in enumerate(contours):
    area_list.append((i, cv2.contourArea(cnt)))
index, maxarea = max(area_list, key=lambda x: x[1])
round(maxarea,2)
```

Calculate the centroid of the maximum area contour and print the result.
```python
M = cv2.moments(contours[index])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx, cy)
```

Calculate the contour approximation for the first contour with epsilon set to 1% of the contour perimeter. Print the number of points in the contour approximation.
```python
epsilon = 0.01 * cv2.arcLength(contours[index], True)
approx = cv2.approxPolyDP(contours[index], epsilon, True)
print(len(approx))
```

Draw the contour approximation on a copy of the original image and display it.
```python
image_approx = cv2.drawContours(image.copy(), [approx], 0, (0,255,0), 3)
plt.imshow(image_approx)
plt.show()
```

Calculate the bounding rectangle for the first contour, draw the rectangle on a copy of the original image and display it.
```python
x, y, w, h = cv2.boundingRect(contours[index])
image_bounding_rect = cv2.rectangle(image.copy(), (x,y), (x+w, y+h), (index,255,0), 2)
plt.imshow(image_bounding_rect)
plt.show()
```

Calculate the minimum enclosing circle for the first contour, draw the circle on a copy of the original image and display it.
```python
(x,y), radius = cv2.minEnclosingCircle(contours[index])
image_enclosing_circle = cv2.circle(image.copy(), (int(x), int(y)), int(radius), (0,255,0), 2)
plt.imshow(image_enclosing_circle)
plt.show()
```