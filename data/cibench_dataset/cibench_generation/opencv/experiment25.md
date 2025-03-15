---
jupyter:
  title: Keypoints Detecting and Matches Finding
  module: opencv
  dataset: lena.png
  difficulty: Middle
  idx: 25
  num_steps: 7
  step_types:
    - exec
    - vis
    - num
    - text
    - exec
    - vis
    - num
  modules: 
    - opencv
    - opencv & matplotlib
    - opencv
    - opencv
    - opencv
    - opencv & matplotlib
    - opencv
---

File Path: 'data/lena.png'.

Load the image from path. Convert the image to grayscale. Initialize the SIFT (Scale-Invariant Feature Transform) detector. Use the SIFT detector to detect keypoints in the grayscale image.
```python
import cv2
img = cv2.imread('data/lena.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
keypoints = sift.detect(gray_img, None)
```

Draw the detected keypoints on the grayscale image. The resulting image (img) will have the keypoints overlaid on it. Display the image with the overlaid keypoints.
```python
import matplotlib.pyplot as plt
img = cv2.drawKeypoints(gray_img, keypoints, img)
plt.imshow(img)
plt.show()
```

Compute the descriptors of the keypoints. The descriptors are a representation of the keypoints that can be used for matching. Print the total number of keypoints detected in the image.
```python
keypoints, descriptors = sift.compute(gray_img, keypoints)
print(len(keypoints))
```

Print the descriptors of the keypoints. These are the unique identifiers for each keypoint.
```python
print(descriptors)
```

Initialize the Brute-Force matcher. This matcher will be used to compare the descriptors and find matches. Use the Brute-Force matcher to find matches between the descriptors. The matcher compares each descriptor with every other descriptor to find matches. Sort the matches based on their distance. The distance is a measure of how similar two descriptors are, with a smaller distance indicating a better match.
```python
bf = cv2.BFMatcher()
matches = bf.match(descriptors, descriptors)
matches = sorted(matches, key=lambda x: x.distance)
```

Draw the top 50 matches on the image. The resulting image (matching_result) will have lines connecting the matched keypoints. Display the image with the matched keypoints.
```python
matching_result = cv2.drawMatches(img, keypoints, img, keypoints, matches[:50], None, flags=2)
plt.imshow(matching_result)
plt.show()
```

Print the total number of matches found by the Brute-Force matcher.
```python
print(len(matches))
```