---
jupyter:
  title: Basic Image Processing with NumPy and SciPy's ndimage
  dataset: None
  difficulty: Easy
  module: scipy
  idx: 38
  num_steps: 5
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
  modules:
    - scipy & numpy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
---

Create a 2D array of zeros with the shape (100, 100). Then, you will define a rectangle of ones inside the array from the 30th to the 70th index along both dimensions. Then define a rectangle of zeros inside the array from the 45th to the 55th index along both dimensions. This will serve as our initial image. Apply a sobel filter to the smoothed image along both dimensions. Then, compute the magnitude of the gradients. Display the magnitude result.

```python
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((100, 100))
image[30:-30, 30:-30] = 1
image[45:55, 45:55] = 0
sx = ndimage.sobel(image, axis=0, mode='constant')
sy = ndimage.sobel(image, axis=1, mode='constant')
mag = np.hypot(sx, sy)
plt.imshow(mag)
plt.show()
```

Apply a binary dilation to the initial image and display the result.

```python
dilated = ndimage.binary_dilation(image)
plt.imshow(dilated)
plt.show()
```

Apply a binary erosion to the initial image and display the result.
```python
eroded = ndimage.binary_erosion(image)
plt.imshow(eroded)
plt.show()
```

Apply a binary closing operation to the initial image and display the result.

```python
closed = ndimage.binary_closing(image)
plt.imshow(closed)
plt.show()
```

Apply a binary fill holes operation to the initial image and display the result.

```python
filled = ndimage.binary_fill_holes(image)
plt.imshow(filled)
plt.show()
```
