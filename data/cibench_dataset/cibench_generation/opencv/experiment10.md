---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: city.mp4
  difficulty: EASY
  idx: 10
  num_steps: 6
  step_types:
    - exec
    - vis
    - vis
    - vis
    - exec
  modules: 
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv
---

File Path: 'data/city.mp4'.


Capture video from the path. Retrieve the first frame from the captured video.
```python
import cv2
video = cv2.VideoCapture('data/city.mp4')
_, first_frame = video.read()
```

Convert the first frame to grayscale. Then, apply Gaussian blur with 21,21 to the converted grayscale image. The Gaussian blur is applied to reduce image noise and reduce detail. Display the blurred grayscale image.
```python
import matplotlib.pyplot as plt
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (21, 21), 0)
plt.imshow(first_gray, cmap='gray')
plt.show()
```
  
Apply a binary threshold to the first frame. All pixel values below 30 are set to 0 (black) and all values above 30 are set to 255 (white). This creates a binary image which makes it easier to detect contours. Then, dilate the threshold frame to further amplify the features in the image. Display the processed image.
```python
thresh_frame = cv2.threshold(first_gray, 30, 255, cv2.THRESH_BINARY)[1]
thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
plt.imshow(thresh_frame, cmap='gray')
plt.show()
```

Find contours in the threshold frame. Iterate over each contour found in the previous step. If the area of the contour is less than 1000, ignore it. Otherwise, indicate that motion has been detected and draw a bounding box around the contour on the original frame. Display the thresh_frame with rectangle.
```python
contours, _ = cv2.findContours(thresh_frame.copy(), 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    if cv2.contourArea(contour) > 1000:
        continue
    motion_detected = 1
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(thresh_frame, (x, y), (x + w, y + h), (0, 255, 128), 3)
plt.imshow(thresh_frame)
plt.show()
```

After breaking the loop, release the video capture.
```python
video.release()
```