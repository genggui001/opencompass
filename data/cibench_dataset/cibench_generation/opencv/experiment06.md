---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 6
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib & numpy
    - opencv & matplotlib
    - opencv & matplotlib
---

File Path: 'data/lena.png'. 

Load the target image in grayscale mode.
```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('data/lena.png', cv2.IMREAD_GRAYSCALE)
```

Apply a Gaussian blur to the image using a kernel size of (5,5) and a standard deviation of 0.
```python
blur = cv2.GaussianBlur(img,(5,5),0)
plt.imshow(blur, cmap='gray')
plt.show()
```
 
Apply the Sobel operator to the blurred image, setting the kernel size to 5 which will detect the edges in the X and Y direction separately. Calculate the magnitude of the gradients obtained from the Sobel operator. Normalize the Magnitude. Visualize the magnitude of the gradients.
```python
import numpy as np
sobelx = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=5)
magnitude = np.hypot(sobelx, sobely)
magnitude *= 255.0 / np.max(magnitude)
plt.imshow(magnitude, cmap='gray')
plt.show()
```

Apply the Canny edge detection algorithm to the blurred image, with lower and upper threshold values of 50 and 150 respectively. Visualize the edges detected by the Canny edge detection algorithm.
```python
edges = cv2.Canny(blur,50,150)
plt.imshow(edges, cmap='gray')
plt.show()
```

Apply the Laplacian operator to the blurred image to detect edges. Visualize the result of the Laplacian operator.
```python
laplacian = cv2.Laplacian(blur,cv2.CV_64F)
plt.imshow(laplacian, cmap='gray')
plt.show()
```

