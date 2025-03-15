---
jupyter:
  title: Basic Image Processing using OpenCV
  module: opencv
  dataset: lena.png
  difficulty: EASY
  idx: 12
  num_steps: 5
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
---

File Path: 'data/lena.png'.

Load an image from a local file.
```python
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('data/lena.png', cv2.IMREAD_COLOR)
```

Convert the color image to a grayscale image and compute the histogram of the grayscale image. Plot the histogram.
```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.show()
```

Compute the histogram for each color channel (Blue, Green, Red) of the original image. Display the histograms for each color channel on the same plot with title 'Color Histograms', xlabel 'Bins' and ylabel 'Number of Pixels'.
```python
color = ('b','g','r')
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.title('Color Histograms')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.show()
```

Improve the contrast of the grayscale image by equalizing its histogram. Display the equalized grayscale image.
```python
eq_image = cv2.equalizeHist(gray_image)
plt.imshow(eq_image, cmap='gray')
plt.title('Equalized Image')
plt.show()
```

Compute the histogram of the equalized image. Plot this histogram. The title is 'Equalized Histogram', xlabel is 'Bins' and ylabel is 'Number of Pixels'.
```python
eq_hist = cv2.calcHist([eq_image], [0], None, [256], [0, 256])
plt.plot(eq_hist)
plt.title('Equalized Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.show()
```
