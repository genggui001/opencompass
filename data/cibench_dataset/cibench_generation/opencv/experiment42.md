---
jupyter:
  title: Stitch 2 Images Together
  module: opencv
  dataset: lena.png, lena1.png, lena2.png
  difficulty: Middle
  idx: 42
  num_steps: 6
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
    - vis
  modules:
    - opencv
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
    - opencv & matplotlib
---

File Path: 'data/lena.png', 'data/lena1.png', 'data/lena2.png'.

Load the lena image from file.
```python
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('data/lena.png')
```

The image is converted to grayscale to reduce its complexity. This aids in reducing processing time and computational resources. A Gaussian Blur is applied to the grayscale image to reduce noise and detail. This helps in smoothing the image and reducing the amount of detail. Edge detection is performed to highlight the main features of the image. This is done using the Canny edge detection method. The edges detected in the previous step are dilated to make them more pronounced. This makes the edges thicker and more visible. The dilated image is then displayed.
```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 30, 150)
dilated = cv2.dilate(edges, None, iterations=2)
plt.imshow(dilated, cmap='gray')
plt.show()
```

Contours in the image are found and drawn on the original image. Display the image with contour.
```python
contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
```

Two images lena1 and lena2 are blended together. The blending is controlled by the alpha 0.5 and beta 0.5 parameters. Display the blending image.
```python
image1 = cv2.imread('data/lena1.png')
image2 = cv2.imread('data/lena2.png')

alpha = 0.5
beta = 0.5
gamma = 0

output = cv2.addWeighted(image1, alpha, image2, beta, gamma)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.show()
```

Two images lena1 and lena2 are stitched together to create a panorama. Display the stitched image.
```python
images = []
images.append(cv2.imread('data/lena1.png'))
images.append(cv2.imread('data/lena2.png'))

stitcher = cv2.Stitcher.create()
status, stitched = stitcher.stitch(images)
plt.imshow(cv2.cvtColor(stitched, cv2.COLOR_BGR2RGB))
plt.show()
```

Fill in the missing areas of an image using image inpainting. This is done by providing a mask that indicates the area to be inpainted.
```python
image = cv2.imread('data/lena.png', cv2.IMREAD_COLOR)
mask = cv2.imread('data/lena.png', cv2.IMREAD_GRAYSCALE)

dst = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()
```