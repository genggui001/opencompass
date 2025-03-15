---
jupyter:
  title: Panoramic Image Stitching with Python
  module: opencv
  dataset: lena1.png, lena2.png
  difficulty: Middle
  idx: 14
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - opencv 
    - opencv & matplotlib
    - opencv & matplotlib & numpy
    - opencv & matplotlib & numpy
    - opencv & matplotlib & numpy
---

File Path: 'data/lena1.png', 'data/lena2.png'.

Load the two images from path. Convert the loaded images to grayscale. Detect ORB (Oriented FAST and Rotated BRIEF) features and compute descriptors for both grayscale images.
```python
import cv2
img1 = cv2.imread('data/lena1.png')
img2 = cv2.imread('data/lena2.png')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
```

Match the descriptors from both images in OpenCV. Sort the matches in ascending order of their distances. Discard matches that are not good enough. Keep only the top 15% of matches. Draw the top matches and display the image.
```python
import matplotlib.pyplot as plt
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(descriptors1, descriptors2, None)
matches = list(matches)
matches.sort(key=lambda x: x.distance, reverse=False)
numGoodMatches = int(len(matches) * 0.15)
matches = matches[:numGoodMatches]
imMatches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches, None)
plt.imshow(imMatches)
plt.show()
```

Extract locations of good matches. Find the homography between the images. . Visualize and display the warped image.
```python
import numpy as np
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)
for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt
h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
height, width, channels = img2.shape
im1Reg = cv2.warpPerspective(img1, h, (width, height))
plt.imshow(im1Reg)
plt.show()
```

Stitch the images together by creating an empty array of zeros and replacing the corresponding values with the pixel values of the images. Visualize and display the stitched image.
```python
panorama = np.zeros((height, width, channels), dtype=np.uint8)
panorama[0:img2.shape[0], 0:img2.shape[1]] = img2
panorama[0:im1Reg.shape[0], 0:im1Reg.shape[1]] = im1Reg
plt.imshow(panorama)
plt.show()
```

Optimize the seam in the final panorama. Visualize and display the image.
```python
mask = 255 * np.ones((img2.shape[0], img2.shape[1]), img2.dtype)
seam_corrected = cv2.seamlessClone(panorama, img2, mask, (img2.shape[1]//2, img2.shape[0]//2) , cv2.NORMAL_CLONE)
plt.imshow(seam_corrected)
plt.show()
```
