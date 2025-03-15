---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 4
  num_steps: 8
  step_types:
    - exec
    - vis
    - vis
    - vis
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
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
---

File Path: 'data/lena.png'. 

Load the image from path.
```python
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('data/lena.png')
```

Convert the image into grayscale. Apply Gaussian Blur to the grayscale image. The kernel size is set as (7, 7) and standard deviation in the X and Y directions (sigmaX and sigmaY) is set as 0. Display the blurred image.
```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
plt.imshow(blurred, cmap='gray')
plt.show()
```

Apply a threshold to the blurred image. The threshold value is set as 225 and the maximum value to use with the THRESH_BINARY_INV thresholding type is set as 255. Perform edge detection on the threshold image. The threshold values are set as 30 and 100. Display the threshold image.
```python
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY_INV)
edges = cv2.Canny(thresh, 30, 100)
plt.imshow(edges, cmap='gray')
plt.show()
```

Find contours in the threshold image. Draw the contours on the original image. The color of the contours is set to green (0, 255, 0) and the thickness is set as 2. Display the contour image.
```python
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.show()
```

Perform image dilation on the edge detected image. The iteration parameter is set as 2. Perform image erosion on the dilated image. The iteration parameter is set as 1. Resize the eroded image to 400x400 pixels. Display the resized image.
```python
dilated = cv2.dilate(edges.copy(), None, iterations=2)
eroded = cv2.erode(dilated.copy(), None, iterations=1)
resized = cv2.resize(eroded, (400, 400))
plt.imshow(resized, cmap='gray')
plt.show()
```

Rotate the original image by -45 degreess. Display the rotated image.
```python
(centerX, centerY) = (image.shape[1] // 2, image.shape[0] // 2)
M = cv2.getRotationMatrix2D((centerX, centerY), -45, 1.0)
rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.show()
```

Perform image cropping on the original image. The cropped region is defined by the pixels 70 to 170 in the y-direction and 440 to 540 in the x-direction. Display a comparison between the original image and the cropped image.
```python
cropped = image[70:170, 440:540]
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[1].imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
axs[1].set_title('Cropped Image')
plt.show()
```

Display a comparison between the original image and the cropped image. The original image should be placed on the left with title 'Original Image' and the cropped image should be placed on the right with title 'Cropped Image'.
```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[1].imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
axs[1].set_title('Cropped Image')
plt.show()
```