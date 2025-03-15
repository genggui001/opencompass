---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 5
  num_steps: 7
  step_types:
    - vis
    - vis
    - vis
    - num
    - vis
    - vis
    - vis
  modules: 
    - opencv & matplotlib & numpy
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib & numpy
---

File Path: 'data/lena.png'. 

Load the image from path. Convert the loaded color image to grayscale. Apply a Gaussian blur to the grayscale image with a kernel size of (5, 5) and standard deviation of 0. Perform edge detection on the blurred image with the lower and upper thresholds of 30 and 150 respectively. Display the edge-detected image.
```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('data/lena.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
edges_img = cv2.Canny(blurred_img, 30, 150)
plt.imshow(edges_img, cmap='gray')
plt.title('Edge Detection')
plt.show()
```

Erode the grayscale image with a structuring element of None and number of iterations set to 2. Display the eroded image.
```python
eroded_img = cv2.erode(gray_img, None, iterations=2)
plt.imshow(eroded_img, cmap='gray')
plt.title('Eroded Image')
plt.show()
```

Dilate the grayscale image with a structuring element of None and number of iterations set to 2. Display the dilated image.
```python
dilated_img = cv2.dilate(gray_img, None, iterations=2)
plt.imshow(dilated_img, cmap='gray')
plt.title('Dilated Image')
plt.show()
```

Use cv2.findContours() function to find the contours in the edge-detected image. Use cv2.RETR_EXTERNAL as the contour retrieval mode and cv2.CHAIN_APPROX_SIMPLE as the contour approximation method. Print the number of contours found.
```python
contours, _ = cv2.findContours(edges_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
```

Draw the contours found in the last step on a copy of the original image. Use green color (0, 255, 0) and thickness of 2. Display the image with drawn contours.
```python
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
# Display the image with drawn contours
plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
plt.title('Contours on Original Image')
plt.show()
```

Rotate the original image by 45 degrees about its centers. Display the rotated image.
```python
rows, cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (cols, rows))
# Display the rotated image
plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
plt.title('Rotated Image')
plt.show()
```

Translate the original image by shifting it 25 pixels to the right and 50 pixels down. Display the translated image.
```python
translation_matrix = np.float32([[1, 0, 25], [0, 1, 50]])
translated_img = cv2.warpAffine(img, translation_matrix, (cols, rows))
plt.imshow(cv2.cvtColor(translated_img, cv2.COLOR_BGR2RGB))
plt.title('Translated Image')
plt.show()
```