---
jupyter:
  title: Demonstration of Various Morphological Operations on a Grayscale Image
  module: opencv
  dataset: lena.png
  difficulty: Middle
  idx: 33
  num_steps: 6
  step_types:
    - exec
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
---

File Path: 'data/lena.png'.

Load the grayscale image from the provided filepath.
```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('data/lena.png',0)
```

Create a 5x5 structuring element or kernel. The first parameter is set to `cv2.MORPH_RECT` to obtain a rectangular kernel. Perform the erosion operation on the image and display.
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
erosion = cv2.erode(img,kernel,iterations = 1)
plt.imshow(erosion, cmap='gray')
plt.show()
```

Perform the opening operation on the image. Set to `cv2.MORPH_OPEN`. Display the image after the opening operation.
```python
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.imshow(opening, cmap='gray')
plt.show()
```

Perform the closing operation on the image. Set to `cv2.MORPH_CLOSE`. Display the image after the closing operation.
```python
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.imshow(closing, cmap='gray')
plt.show()
```

Perform the morphological gradient operation on the image. Set to `cv2.MORPH_GRADIENT`. Display the image after the gradient operation.
```python
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.imshow(gradient, cmap='gray')
plt.show()
```

Perform the top hat operation on the image. Set to `cv2.MORPH_TOPHAT`. Display the image after the top hat operation.
```python
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
plt.imshow(tophat, cmap='gray')
plt.show()
```
