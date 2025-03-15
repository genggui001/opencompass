---
jupyter:
  title: Apply the Background Subtractor to the video
  module: opencv
  dataset: city.mp4
  difficulty: Middle
  idx: 23
  num_steps: 8
  step_types:
    - exec
    - exec
    - vis
    - vis
    - vis
    - vis
    - vis
    - exec
  modules: 
    - opencv  
    - opencv 
    - matplotlib
    - matplotlib 
    - opencv & matplotlib
    - opencv & matplotlib & numpy
    - opencv & matplotlib 
    - opencv
---

File Path: 'data/city.mp4'.


Load video file from path. Create a background subtractor.
```python
import cv2
cap = cv2.VideoCapture('data/city.mp4')
bg_subtractor = cv2.createBackgroundSubtractorMOG2()
```

Start a loop that continues until the video ends. Apply the background subtractor to each frame using the apply method. This will produce a mask where the moving objects are white and the background is black.
```python
while(1):
    ret, frame = cap.read()
    if ret == True:
        break
fg_mask = bg_subtractor.apply(frame)
```

Using matplotlib, display the original last frame of the video.
```python
import matplotlib.pyplot as plt
plt.imshow(frame[:,:,::-1])
plt.show()
```

Also, display the foreground mask using a grayscale colormap.
```python
plt.imshow(fg_mask, cmap='gray')
plt.show()
```

Apply a binary threshold to the foreground mask. This will convert all the pixel values above 127 to 255 (white) and those below to 0 (black). Display the thresholded mask using a grayscale colormap.
```python
_, thresh = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY)
plt.imshow(thresh, cmap='gray')
plt.show()
```

Apply morphological operations (erosion and dilation) to the thresholded mask to remove any noise. This is done using a 5x5 kernel (a small matrix used for transformations). We perform one iteration of erosion (which shrinks white object pixels) followed by two iterations of dilation (which expands them). Display the result after the morphological operations using a grayscale colormap.
```python
import numpy as np
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 2)
plt.imshow(dilation, cmap='gray')
plt.show()
```

Detect the contours of the objects in the image. Draw these contours on the original video frame. The contours will be drawn in green color with a thickness of 3 pixels. Finally, display the original frame with the contours overlaid.
```python
contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(frame, contours, -1, (0,255,0), 3)
plt.imshow(frame)
plt.show()
```

Release the video capture .
```python
cap.release()
```