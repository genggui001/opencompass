---
jupyter:
  title: Image Processing Experiment on Raccoon Face Grayscale Conversion and Filter Impact Analysis
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 12
  num_steps: 3
  step_types:
    - vis
    - vis
    - vis
  modules: 
    - numpy & scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
---

Load the built-in raccoon face image from scipy.misc library. Convert it to gray scale use [0.2989, 0.5870, 0.1140] weight for RGB. Display the gray image.
```python
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
face = misc.face()

face_gray = np.dot(face[...,:3], [0.2989, 0.5870, 0.1140])
plt.imshow(face_gray, cmap='gray')
plt.show()
```

Apply a median filter to the grayscale image with a size of 10. Display the resulting image.
```python
from scipy.ndimage import median_filter

face_median = median_filter(face_gray, size=10)
plt.imshow(face_median, cmap=plt.get_cmap('gray'))
plt.show()
```

Apply a Gaussian filter to the grayscale image with a sigma of 10. Display the resulting image.
```python
from scipy.ndimage import gaussian_filter

face_gaussian = gaussian_filter(face_gray, sigma=10)
plt.imshow(face_gaussian, cmap=plt.get_cmap('gray'))
plt.show()
```
