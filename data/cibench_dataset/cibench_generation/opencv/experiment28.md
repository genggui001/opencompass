---
jupyter:
  title: Use multiple images of a chessboard taken at different angles to accurate camera calibration
  module: opencv
  dataset: board.png
  difficulty: Middle
  idx: 28
  num_steps: 5
  step_types:
    - exec
    - vis
    - exec
    - exec
    - vis
  modules: 
    - numpy 
    - opencv & matplotlib
    - opencv 
    - opencv 
    - matplotlib
---

File Path: 'data/board.png'.

Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(7,4,0). Also initialize arrays to store object points and image points from all the images.
```python
import numpy as np
objp = np.zeros((5*8,3), np.float32)
objp[:,:2] = np.mgrid[0:5,0:8].T.reshape(-1,2)
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.
```

Read all the chessboard images and convert them to grayscale. Identify the corners of the chessboard. If corners are found, add object points, image points (after refining them).  draw the corners on the image and display it.
```python
import glob
import cv2
import matplotlib.pyplot as plt
images = glob.glob('data/board*')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (8,5), None)
    if ret == True:
       objpoints.append(objp)
       imgpoints.append(corners)
    img = cv2.drawChessboardCorners(img, (8,5), corners, ret)
    plt.imshow(img)
plt.show()
```

Obtain the camera matrix and distortion coefficients.
```python
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
```

Correct for lens distortion in the image.
```python
img = cv2.imread('data/board.png')
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
```

Crop the image according to the region of interest.
```python
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
plt.imshow(dst)
plt.show()
```


