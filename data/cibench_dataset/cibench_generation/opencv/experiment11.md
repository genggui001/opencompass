---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 11
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - exec
    - text
  modules: 
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv 
    - opencv
---

File Path: 'data/lena.png'.

Load an image from a local file.
```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('data/lena.png')
```

As OCR performs better on grayscale images, convert the loaded image to grayscale. Apply thresholding to the grayscale image. Display the threshold image.
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
plt.imshow(thresh1, cmap='gray')
plt.show()
```

Define the structure shape and kernel size, which will be used for dilation. Use arguments cv2.MORPH_RECT and (18, 18). Apply dilation to the threshold image using the rectangular kernel defined in the previous step. This operation highlights the region where the text is present. Display the dilated image.
```python
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilated = cv2.dilate(thresh1, rect_kernel, iterations = 1)
plt.imshow(dilated, cmap='gray')
plt.show()
```

Find contours in the image. Contours are curves joining all the continuous points (along the boundary), having the same color or intensity. Sort the contours in order to read the text from left to right, top to bottom. Use Python's inbuilt sorted function.
```python
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key = lambda x: (cv2.boundingRect(x)[1], cv2.boundingRect(x)[0]))
```

Iterate over all the contours, calculate the area of rectangle of each contour.
```python
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cropped = thresh1[y:y + h, x:x + w]
    print(h*w)
```
