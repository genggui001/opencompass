---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 1
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
    - opencv & matplotlib & numpy
    - opencv & matplotlib & numpy
    - opencv & matplotlib
    - opencv & matplotlib & numpy
---

File Path: 'data/lena.png'. 

Read the image from the path.
```python
import cv2
img = cv2.imread('data/lena.png')
```

Convert the color image to grayscale. Display the grayscale image setting the color map to 'gray'.
```python
import matplotlib.pyplot as plt
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.show()
```

Apply Gaussian blur to the grayscale image. Provide the grayscale image, kernel size as (5, 5), and sigma value as 0 as the input parameters. Display the blurred image.
```python
blur = cv2.GaussianBlur(gray, (5, 5), 0)
plt.imshow(blur, cmap='gray')
plt.show()
```

Perform edge detection on the blurred image. Provide the blurred image and thresholds as 50 and 150 as input parameters. Display the edges detected.
```python
edges = cv2.Canny(blur, 50, 150)
plt.imshow(edges, cmap='gray')
plt.show()
```

Perform image dilation on the edge-detected image. Create a (2,2) kernel and dilate the image. Display the dilated image.
```python
import numpy as np
kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(edges, kernel, iterations = 1)
plt.imshow(dilation, cmap='gray')
plt.show()
```

Perform image erosion on the dilated image. Create a (1,1) kernel and erode the image. Display the eroded image.
```python
kernel = np.ones((1,1),np.uint8)
erosion = cv2.erode(dilation, kernel, iterations = 1)
plt.imshow(erosion, cmap='gray')
plt.show()
```

Draw contours on the original image. Find contours and draw the contours on the original image. Display the image with contours.
```python
contours, _ = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoured = cv2.drawContours(img, contours, -1, (0,255,0), 3)
plt.imshow(cv2.cvtColor(contoured, cv2.COLOR_BGR2RGB))
plt.show()
```

Perform image segmentation on the original image. Use OpenCV to perform image segmentation. Display the segmented image.
```python
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img_segmented = img*mask2[:,:,np.newaxis]
plt.imshow(cv2.cvtColor(img_segmented, cv2.COLOR_BGR2RGB))
plt.show()
```