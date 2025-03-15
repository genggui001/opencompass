---
jupyter:
  title: Loading a video, extracting frames, and converting those frames to grayscale
  module: opencv
  dataset: city.mp4
  difficulty: Middle
  idx: 44
  num_steps: 7
  step_types:
    - num
    - vis
    - num
    - vis
    - exec
  modules:
    - opencv 
    - opencv & matplotlib
    - opencv 
    - opencv & matplotlib
    - opencv 
---

File Path: 'data/city.mp4'.

First, we need to load the video file for processing. After loading the video, we can check the total number of frames with `cv2.CAP_PROP_FRAME_COUNT` as the argument. Print the total number of frames.
```python
import cv2
cap = cv2.VideoCapture('data/city.mp4')
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
total_frames
```

Display the frame on frame 100.
```python
import matplotlib.pyplot as plt
cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
ret, frame = cap.read()
plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
plt.show()
```

Extract every 100th frame from the video to a list. Display the length of the list.
```python
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
frame_id = 0
images = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_id % 100 == 0:
        images.append(frame)
    frame_id += 1
len(images)  
```

Here, we create a 2x2 subplot and display each frame in a separate subplot.
```python
fig = plt.figure(figsize=(10, 10))
for i, img in enumerate(images):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
```


Release the video file to free up system resources.
```python
cap.release()
```