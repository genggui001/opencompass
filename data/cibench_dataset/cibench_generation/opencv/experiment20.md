---
jupyter:
  title: Process an image to extract and analyze the text it contains
  module: opencv
  dataset: lena.png
  difficulty: Middle
  idx: 20
  num_steps: 4
  step_types:
    - exec
    - vis
    - vis
    - vis
  modules: 
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib 
---

File Path: 'data/lena.png'.

Load the image in grayscale mode.
```python
import cv2
img = cv2.imread('data/lena.png',0)
```

Convert the grayscale image to binary use threshold with 127 as the threshold value and 255 as the maximum value. The binary threshold type is used. Display the image.
```python
import matplotlib.pyplot as plt
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap='gray')
plt.show()
```

Remove the noise from the binary image. The kernel size is set to 5. Display the image.
```python
blur = cv2.medianBlur(thresh1,5)
plt.imshow(blur, cmap='gray')
plt.show()
```

Detect contour in the external mode with the simple chain approximation method. Draw bounding boxes around the detected text.
```python
contours, hierarchy = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
plt.imshow(img, cmap='gray')
plt.show()
```
