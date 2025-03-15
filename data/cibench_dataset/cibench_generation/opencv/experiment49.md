---
jupyter:
  title: 3D Model Recognition in 2D Images using SIFT and FLANN in Python
  module: opencv
  dataset: chess.png, board.png
  difficulty: Middle
  idx: 49
  num_steps: 5
  step_types:
    - exec
    - exec
    - exec
    - exec
    - vis
  modules: 
    - opencv
    - opencv 
    - opencv 
    - opencv
    - opencv & matplotlib
---

File Path: 'data/chess.png', 'data/board.png'.

Load the two image in gray scale.
```python
import cv2
import matplotlib.pyplot as plt
model = cv2.imread('data/chess.png', 0)
image = cv2.imread('data/board.png', 0)
```

Initiate the SIFT detector. Use the SIFT detector to find the keypoints and descriptors in both the 3D model and the 2D image.
```python
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(model,None)
kp2, des2 = sift.detectAndCompute(image,None)
```

Define the FLANN index parameters and search parameters. Set the algorithm to FLANN_INDEX_KDTREE and trees to 5. The checks parameter is set to 50 for search parameters. Configure the FLANN based matcher with the defined parameters.
```python
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)
```

Use the FLANN based matcher to match the descriptors of the 3D model and the 2D image. Store all the good matches as per Lowe's ratio test.
```python
matches = flann.knnMatch(des1,des2,k=2)
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
```

Draw the matches between the 3D model and the 2D image. Display the image with the matches.
```python
draw_params = dict(matchColor = (0,255,0),  # draw matches in green color
                   singlePointColor = None,
                   flags = 2)
img3 = cv2.drawMatches(model,kp1,image,kp2,good,None,**draw_params)
plt.imshow(img3, 'gray')
plt.show()
```