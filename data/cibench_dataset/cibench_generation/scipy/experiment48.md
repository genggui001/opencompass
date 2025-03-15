---
jupyter:
  title: Image Processing using SciPy and Matplotlib
  module: SciPy
  dataset: none
  difficulty: MIDDLE
  idx: 48
  num_steps: 3
  step_types:
    - vis
    - vis
    - vis
  modules: 
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
---

Get the ascent image from the scipy library. Apply a median filter with size 3 to the image and display the result.
```python
from scipy import ndimage, misc
import matplotlib.pyplot as plt
image = misc.ascent()
median_filtered = ndimage.median_filter(image, size=3)
plt.imshow(median_filtered, cmap='gray')
plt.show()
```

Rotate the image by 45 degrees and shift the image by 50 pixels in both the x and y directions. Display the shifted image.
```python
rotated = ndimage.rotate(image, 45)
shifted = ndimage.shift(rotated, (50, 50))
plt.imshow(shifted, cmap='gray')
plt.show()
```

Zoom into the original image by a factor of 2. Display the zoomed image.
```python
zoomed = ndimage.zoom(image, 2)
plt.imshow(zoomed, cmap='gray')
plt.show()
```
