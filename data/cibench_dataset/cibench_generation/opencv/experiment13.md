---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 13
  num_steps: 6
  step_types:
    - exec
    - vis
    - num
    - text
    - text
    - vis
  modules: 
    - opencv 
    - opencv & matplotlib
    - opencv
    - opencv
    - opencv
    - opencv & matplotlib
---

File Path: 'data/lena.png'.

Load the image from file path. Convert it to gray scale. Initialize the ORB feature detector object. 
```python
import cv2
img = cv2.imread('data/lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
```

Detect the keypoints in the grayscale image by calling the detect method on the orb object and passing the grayscale image as its parameter. Compute the descriptors of the detected keypoints. Descriptors are used to match keypoints between different images. Call the compute method on the orb object with the grayscale image and keypoints as parameters. Visualize the detected keypoints by drawing them on the original image. The color parameter is set to green (0,255,0) and flags are set to 0. Display the image with the keypoints drawn on it.
```python
import matplotlib.pyplot as plt
kp = orb.detect(gray, None)
kp, des = orb.compute(gray, kp)
img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2)
plt.show()
```

Print the total number of keypoints detected by the orb detector.
```python
print(len(kp))
```

Print the shape of the descriptor to understand its dimensionality.
```python
print(des.shape)
```

Print the first descriptor to get a sense of the values.
```python
print(des[0])
```

Initialize the FLANN matcher with the LSH (Locality-Sensitive Hashing) algorithm. The table_number and key_size parameters affect the performance and accuracy of the matching. Filter out good matches using the ratio test proposed by D.Lowe in his paper. This test removes poor matches based on the ratio of the distances of the two best matches. Draw the good matches on the image. The flags parameter is set to 2 to draw only the good matches. Display the image with the good matches drawn on it.
```python
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6,
                   key_size = 12,
                   multi_probe_level = 1)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des, des, k=2)
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append([m])
img3 = cv2.drawMatchesKnn(img,kp,img,kp,good,None,flags=2)
plt.imshow(img3)
plt.show()
```