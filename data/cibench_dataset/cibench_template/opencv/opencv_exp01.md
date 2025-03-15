---
jupyter:
  title: Basic processing, contour detection and corner detection of image
  module: opencv
  dataset: book image
  difficulty: Middle
  idx: 1
  num_steps: 6
  step_types:
    - exec
    - vis
    - num
    - vis
    - vis
    - vis
  modules: 
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & numpy
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & numpy 
---

File Path: 'data/opencv_dataset01.jpg'. 
### Load the image from the file path. Display the original RGB image.
```python
import cv2
import matplotlib.pyplot as plt
file_path = 'data/opencv_dataset01.jpg'
image = cv2.imread(file_path)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
```

### Resize the image to (500,560). Convert the image to grayscale and display the converted image.
```python
resized_image = cv2.resize(image, (500, 560))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.show()
```

### Set the Guass kernel size as (3,3) and Guass sigma as 0, apply Guassian blur to the grayscale image. Set the target size as (500,600) and then perform Linear interpolation on the blurred image. Calculate the mean value of the resultant image pixels. Print the result with two decimal places.
```python
import numpy as np
gaussian_kernel_size = (3, 3)
gaussian_sigma = 0
blurred_image = cv2.GaussianBlur(gray_image, gaussian_kernel_size, gaussian_sigma)
target_size = (500, 600)
resized_image = cv2.resize(blurred_image, target_size, interpolation=cv2.INTER_LINEAR)
mean_value = np.mean(resized_image)
round(mean_value,2)
```

### Applying histogram equalization to the blurred grayscale image to enhance its contrast, followed by displaying the resultant image.
```python
equalized_image = cv2.equalizeHist(blurred_image)
plt.imshow(equalized_image, cmap='gray')
plt.show()
```

### Detect edges using the Canny edge detector with canny min-val=80 and canny max-val=200 on the image processed in the previous step. Display the edged image.
```python
canny_min_val = 80
canny_max_val = 200
edges = cv2.Canny(equalized_image, canny_min_val, canny_max_val)
plt.imshow(edges, cmap='gray')
plt.show()
```

### Detect corners using the Shi-Tomas corner detector with max-corners=50, min-distance=0.5 and blocksize=10, mark the corners with circles on the image. Note that the coordinates of corner points must be a tuple of integers. The radius and thickness of the circle are 5 and 1. Show the marked image.
```python
max_corners = 50
min_distance = 0.5
block_size = 10
corners = cv2.goodFeaturesToTrack(equalized_image, max_corners, 0.01, min_distance, blockSize=block_size)
corners = np.intp(corners)

marked_image = resized_image.copy()
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(marked_image, (x, y), 5, (0, 0, 255), 1)  #circle with radius 5 and thickness 1

plt.imshow(cv2.cvtColor(marked_image, cv2.COLOR_BGR2RGB))
plt.show()
```

