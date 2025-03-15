---
jupyter:
  title: Draw square on the image
  module: opencv
  dataset: lena.png
  difficulty: Middle
  idx: 16
  num_steps: 7
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis
  modules: 
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib & numpy
    - opencv & matplotlib
    - opencv & matplotlib & numpy
    - opencv & matplotlib 
    - opencv & matplotlib
---

File Path: 'data/lena.png'.

Load the image from path in grayscale.
```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('data/lena.png', 0)
```

Detect the edges in the image. Set threshold to 100 and 200. Visualize the edge detected image.
```python
edges = cv2.Canny(img, 100, 200)
plt.imshow(edges, cmap='gray')
plt.show()
```

Find contours in the edge detected image. Create a blank image with the same dimensions as the original image. Draw the contours on the blank image with red line with 3 thickness.
```python
import numpy as np
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = np.zeros_like(img)
cv2.drawContours(img_contours, contours, -1, (255,0,0), 3)
plt.imshow(img_contours, cmap='gray')
plt.show()
```

From the list of contours, select the one with the largest area. Compute the bounding rectangle of the largest area contour. Draw the bounding rectangle on a copy of the original image. Visualize the image with the bounding rectangle.
```python
contour = max(contours, key = cv2.contourArea)
x, y, w, h = cv2.boundingRect(contour)
img_bounding_box = cv2.rectangle(img.copy(), (x, y), (x+w, y+h), (255,0,0), 2)
plt.imshow(img_bounding_box, cmap='gray')
plt.show()
```

Compute the perspective transform matrix. Apply the perspective transform to the image. Visualize the transformed image.
```python
pts1 = np.float32([[x, y], [x+w, y], [x+w, y+h], [x, y+h]])
pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_transformed = cv2.warpPerspective(img, matrix, (w, h))
plt.imshow(img_transformed, cmap='gray')
plt.show()
```

Create a 3D cube. The cube is represented as a list of its vertices. Draw the cube on a copy of the original images. Visualize the image with the drawn cube.
```python
img_cube = img.copy()
cube = np.array([[[50, 50, 0], [150, 50, 0], [150, 150, 0], [50, 150, 0], [100, 100, 100]]], dtype=np.float32)
cube_2d = cube[:, :, :2].astype(np.int32)
cv2.polylines(img_cube, [cube_2d[0, :4]], isClosed=True, color=(0, 255, 0), thickness=2)
for i in range(4):
    cv2.line(img_cube, tuple(cube_2d[0, i]), tuple(cube_2d[0, 4]), (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(img_cube, cv2.COLOR_BGR2RGB))
plt.show()
```


Overlay the cube onto the original image with the WARP_INVERSE_MAP flag. Visualize the final result.
```python
img_result = cv2.warpPerspective(img_cube, matrix, (img.shape[1], img.shape[0]), img.copy(), cv2.WARP_INVERSE_MAP)
plt.imshow(img_result, cmap='gray')
plt.show()
```
