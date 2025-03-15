---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 2
  num_steps: 6
  step_types:
    - text
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - opencv & urlib & numpy
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - matplotlib
---

File Path: 'data/lena.png'. 

Read the image from the path. Print the shape and datatype.
```python
import cv2
import urllib.request
import numpy as np
img = cv2.imread('data/lena.png')

print('Shape:', img.shape)
print('Datatype:', img.dtype)
```

For visualization using Matplotlib, we need to convert the bgr image to RGB format. Display the original image (in BGR format) and the converted image (in RGB format) side by side using Matplotlib.
```python
from matplotlib import pyplot as plt
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.title('BGR')
plt.subplot(122), plt.imshow(img_rgb), plt.title('RGB')
plt.show()
```

Split the RGB image into its individual color channels (red, green, and blue) and then merge them back. Then visualize the individual color channels: red, green, and blue.
```python
r, g, b = cv2.split(img_rgb)
img_merged = cv2.merge([r, g, b])
plt.subplot(131), plt.imshow(r, cmap='Reds'), plt.title('Red')
plt.subplot(132), plt.imshow(g, cmap='Greens'), plt.title('Green')
plt.subplot(133), plt.imshow(b, cmap='Blues'), plt.title('Blue')
plt.show()
```

Convert the RGB image to grayscale. Then normalize the pixel values of the grayscale image to a range of 0 to 1. Display the normalized grayscale image:
```python
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_normalized = cv2.normalize(img_gray, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
plt.imshow(img_normalized, cmap='gray'), plt.title('Normalized Grayscale')
plt.show()
```

Apply a binary threshold to the grayscale image. This will convert all pixels to either black or white, depending on whether they are above or below the threshold value of 127. Then perform histogram equalization on the grayscale image to improve its contrast and display the equalized grayscale image
```python
ret, img_thresholded = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
img_equalized = cv2.equalizeHist(img_gray)
plt.imshow(img_equalized, cmap='gray'), plt.title('Equalized Grayscale')
plt.show()
```

Finally, Display the original image, the grayscale image, the thresholded image, and the equalized image side by side for comparison.
```python
plt.subplot(141), plt.imshow(img_rgb), plt.title('Original')
plt.subplot(142), plt.imshow(img_gray, cmap='gray'), plt.title('Grayscale')
plt.subplot(143), plt.imshow(img_thresholded, cmap='gray'), plt.title('Thresholded')
plt.subplot(144), plt.imshow(img_equalized, cmap='gray'), plt.title('Equalized')
plt.show()
```