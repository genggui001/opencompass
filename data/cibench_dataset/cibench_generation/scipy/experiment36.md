---
jupyter:
  title: None
  module: SciPy
  dataset: None
  difficulty: EASY
  idx: 36
  num_steps: 6
  step_types:
    - vis
    - vis
    - vis
    - vis
    - num
    - num
  modules: 
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy & matplotlib
    - scipy
    - numpy & scipy
---

Use an inbuilt image 'ascent' from the scipy's misc module. Apply a Gaussian filter with a sigma value of 3 to the original image. Display the processed image.
```python
from scipy.misc import ascent
import matplotlib.pyplot as plt

image = ascent()
import scipy.ndimage as ndi

filtered_image = ndi.gaussian_filter(image, sigma=3)
plt.imshow(filtered_image, cmap='gray')
plt.show()
```

Calculate the gradient magnitude of the filtered image with a sigma value of 3. Display the processed image.
```python
sigma = 3 
gradient_image = ndi.gaussian_gradient_magnitude(filtered_image, sigma=sigma)
plt.imshow(gradient_image, cmap='gray')
plt.show()
```

Threshold the gradient image to create a binary image. In this step, any pixel value below 10 is set to 0 (making it black), and any value above 10 is set to 255 (making it white). Display the processed image.
```python
threshold_image = gradient_image > 10
plt.imshow(threshold_image, cmap='gray')
plt.show()
```

Perform a binary opening operation on the thresholded image with a structuring element of size 3. Display the processed image.
```python
import numpy as np

opened_image = ndi.binary_opening(threshold_image, structure=np.ones((3,3)))
plt.imshow(opened_image, cmap='gray')
plt.show()
```

Label the connected components in the smoothened image. Display the number of connected components.
```python
label_image, n_labels = ndi.label(opened_image)
n_labels
```

Filter out small components in the labeled image based on their size. Compute the size of each component and create a mask that only includes components with size larger than 10. And calculate the centroid of each region in the cleaned image. Display the number of valid centroids.
```python
sizes = ndi.sum(opened_image, label_image, range(n_labels + 1))
mask_size = sizes > 10
clean_image = mask_size[label_image]
centroids = ndi.center_of_mass(clean_image, labels=label_image, index=range(1, n_labels+1))
sum([ not np.isnan(i[0]) for i in centroids])
```
