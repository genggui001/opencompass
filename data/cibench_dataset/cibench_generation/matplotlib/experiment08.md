---
jupyter:
  title: Image Processing of a House Sparrow Picture
  module: matplotlib
  dataset: none
  difficulty: MIDDLE
  idx: 8
  num_steps: 6
  step_types:
    - vis
    - vis
    - vis
    - vis
    - vis
    - vis   
  modules: 
    - matplotlib & PIL
    - matplotlib & PIL
    - matplotlib
    - matplotlib
    - matplotlib
    - matplotlib
---

File Path: "data/matplotlib_dataset08_your_image.jpg".

Load the image from path and show.
```python
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('data/matplotlib_dataset08_your_image.jpg')
plt.imshow(img)
plt.show()
```

Convert the image into a grayscale format and display the grayscale image.
```python
gray_img = img.convert('L')
plt.imshow(gray_img, cmap='gray')
plt.show()
```

Apply a threshold of 128 to the grayscale image to create a binary image. In this binary image, pixels with values lower than 128 will be set to 0 (black) and those with values higher than 128 will be set to 255 (white).
```python
threshold = 128
binary_img = gray_img.point(lambda p: p > threshold and 255)
plt.imshow(binary_img, cmap='gray')
plt.show()
```

Separate the Red, Green, and Blue channels of the image and display these channels separately.
```python
import numpy as np
img_array = np.array(img)
fig, axs = plt.subplots(1, 3, figsize=(15,5))
for i, (name, color) in enumerate(zip(('Red', 'Green', 'Blue'), ('Reds', 'Greens', 'Blues'))):
    axs[i].imshow(img_array[:,:,i], cmap=color)
    axs[i].set_title(name)
plt.show()
```

Convert the image from RGB to HSV (Hue, Saturation, Value) color space and display the HSV channels separately.
```python
from matplotlib.colors import rgb_to_hsv
hsv_img = rgb_to_hsv(img_array / 255.)
fig, axs = plt.subplots(1, 3, figsize=(15,5))
for i, name in enumerate(('Hue', 'Saturation', 'Value')):
    axs[i].imshow(hsv_img[:,:,i], cmap='gray' if i == 2 else None)
    axs[i].set_title(name)
plt.show()
```

Rotate the image 45 degrees counterclockwise and display the rotated image.
```python
rot_img = img.rotate(45)
plt.imshow(rot_img)
plt.show()
```