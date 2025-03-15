---
jupyter:
  title: Advanced Image Processing Techniques on a House Sparrow Image.
  module: matplotlib
  dataset: https://upload.wikimedia.org/wikipedia/commons/3/32/House_sparrow04.jpg
  difficulty: MIDDLE
  idx: 42
  num_steps: 4
  step_types:
    - vis
    - vis
    - vis
    - vis
  modules: 
    - numpy & matplotlib
    - matplotlib
    - matplotlib
    - scipy & matplotlib
---

File Path: "data/matplotlib_dataset42_House_sparrow04.jpg".

Read the image from the provided URL and save it as a numpy array.Then convert the image from the RGB color space to grayscale using the formula `0.2989 * R + 0.5870 * G + 0.1140 * B`. Display the gray scale image.
```python
import matplotlib.image as mpimg
img = mpimg.imread('data/matplotlib_dataset42_House_sparrow04.jpg')
import matplotlib.pyplot as plt
import numpy as np
grayscale = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
plt.imshow(grayscale, cmap=plt.get_cmap('gray'))
plt.show()
```

Plot a histogram of the pixel intensities of the grayscale image.
```python
plt.hist(grayscale.ravel(), bins=256, color='gray')
plt.show()
```

Apply a color map to the grayscale image. Use nipy spectral.
```python
imgplot = plt.imshow(grayscale)
imgplot.set_cmap('nipy_spectral')
plt.show()
```

Apply the Sobel filter to the grayscale image for edge detection.
```python
from scipy import ndimage
dx = ndimage.sobel(grayscale, 0)
dy = ndimage.sobel(grayscale, 1)
mag = np.hypot(dx, dy)
mag *= 255.0 / np.max(mag)
plt.imshow(mag, cmap='gray')
plt.show()
```
