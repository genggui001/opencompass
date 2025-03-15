---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 3
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
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
---

File Path: 'data/lena.png'. 

Load an image from a local file.
```python
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('data/lena.png')
```

Convert the loaded image to grayscale. Display the grayscale image.
```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.show()
```

Apply a Gaussian blur to the grayscale image. Use a kernel size of (5, 5) for the Gaussian blur. Display the blurred image.
```python
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
plt.imshow(blurred_image, cmap='gray')
plt.show()
```

Perform edge detection on the blurred image using the Canny algorithm. Use 50 and 150 as the lower and upper threshold values for the hysteresis procedure. Display the result of the edge detection.
```python
edges = cv2.Canny(blurred_image, 50, 150)
plt.imshow(edges, cmap='gray')
plt.show()
```

Perform dilation on the edge-detected image to close gaps between object edges. Perform two iterations of dilation. Then perform erosion on the dilated image. Perform one iteration of erosion. Display the result of the dilation and erosion.
```python
dilated_image = cv2.dilate(edges, None, iterations=2)
eroded_image = cv2.erode(dilated_image, None, iterations=1)
plt.imshow(eroded_image, cmap='gray')
plt.show()
```
