---
jupyter:
  title: Process an Image of a Hand Gesture
  module: opencv
  dataset: hand.png
  difficulty: Middle
  idx: 24
  num_steps: 6
  step_types:
    - exec
    - exec
    - exec
    - exec
    - num
    - vis
  modules: 
    - opencv
    - opencv 
    - opencv
    - opencv
    - numpy
    - opencv & matplotlib
---

File Path: 'data/hand.png'.

Load the image from the file path and convert to gray scale.
```python
import cv2
import numpy as np
hand_img = cv2.imread('data/hand.png')
gray = cv2.cvtColor(hand_img, cv2.COLOR_BGR2GRAY)
```

Apply a Gaussian blur to the grayscale image. Use a 5x5 kernel and a sigma (standard deviation) of 0. Apply a binary inverse threshold to the blurred image. Use 70 as the threshold value, 255 as the max value, and the flag cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU.
```python
blur = cv2.GaussianBlur(gray, (5,5), 0)
ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
```

Find the contours in the threshold image. Use cv2.RETR_TREE as the contour retrieval mode and cv2.CHAIN_APPROX_SIMPLE as the contour approximation method. Identify the contour with the maximum area in combination to calculate the area of each contour (using cv2.contourArea).
```python
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key = lambda x: cv2.contourArea(x))
```

Approximate the contour and find its convex hull. The convex hull is the smallest convex polygon that contains all the points of the contour. Use 0.0005*cv2.arcLength(cnt,True) as the precision parameter in cv2.approxPolyDP. Find the convexity defects of the contour. These are the deviations of the contour from its convex hull.
```python
epsilon = 0.0005*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
hull = cv2.convexHull(cnt)
hull2 = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull2)
```

Count the number of convexity defects. This number can be used to determine the gesture represented by the hand in the image. Loop through each defect, calculate the angle formed by the start, end, and far point of each defect, and increment the count if the angle is less than or equal to 90 degrees. Display the number of defects.
```python
defects_count = 0
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    a = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    b = np.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    c = np.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
    angle = np.arccos((b**2 + c**2 - a**2)/(2*b*c))
    if angle <= np.pi/2:
        defects_count += 1
defects_count
```

Draw the approximated contour and the convex hull on the original image. Use (0, 255, 0) for the color of the approximated contour and (0, 0, 255) for the color of the convex hull. Both should have a thickness of 2. Finally, display the image with the drawn contours.
```python
import matplotlib.pyplot as plt
cv2.drawContours(hand_img, [approx], -1, (0, 255, 0), 2)
cv2.drawContours(hand_img, [hull], -1, (0, 0, 255), 2)
plt.imshow(hand_img)
plt.show()
```