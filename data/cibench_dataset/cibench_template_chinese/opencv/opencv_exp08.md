---
jupyter:
  title: 图像的基本处理、轮廓检测和角点检测
  module: opencv
  dataset: 花朵图像
  difficulty: 中级
  idx: 8
  num_steps: 6
  step_types:
     - exec
     - vis
     - num
     - vis
     - vis
     - vis
  modules: 
     - opencv 和 matplotlib
     - opencv 和 matplotlib
     - opencv 和 numpy
     - opencv 和 matplotlib
     - opencv 和 matplotlib
     - opencv 和 numpy
   
---

文件路径：'data/opencv_dataset08.jpg'. 
### 从文件路径加载图像。显示原始的 RGB 图像。
```python
import cv2
import matplotlib.pyplot as plt
file_path = 'data/opencv_dataset08.jpg'
image = cv2.imread(file_path)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
```

### 调整图像大小为 (500, 560)。将图像转换为灰度图并显示转换后的图像。
```python
resized_image = cv2.resize(image, (500, 560))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.show()
```

### 将高斯核大小设置为 (3,3)，高斯标准差设置为 0，对灰度图像应用高斯模糊。将目标大小设置为 (500,600)，然后对模糊图像执行线性插值。计算结果图像像素的平均值，打印保留两位小数后的结果。
```python
import numpy as np
gaussian_kernel_size = (3, 3)
gaussian_sigma = 0
blurred_image = cv2.GaussianBlur(gray_image, gaussian_kernel_size, gaussian_sigma)
target_size = (500, 600)
resized_image = cv2.resize(blurred_image, target_size, interpolation=cv2.INTER_LINEAR)
mean_value = np.mean(resized_image)
round(mean_value,2)
```

### 对模糊的灰度图像应用直方图均衡化以增强对比度，然后显示结果图像。
```python
equalized_image = cv2.equalizeHist(blurred_image)
plt.imshow(equalized_image, cmap='gray')
plt.show()
```

### 使用 Canny 边缘检测器在前一步处理的图像上进行边缘检测，设置 Canny 最小值为 80，最大值为 200。显示边缘图像。
```python
canny_min_val = 80
canny_max_val = 200
edges = cv2.Canny(equalized_image, canny_min_val, canny_max_val)
plt.imshow(edges, cmap='gray')
plt.show()
```

### 使用 Shi-Tomas 角点检测器检测角点，设置最大角点数为 50，最小距离为 0.5，块大小为 10。在图像上用圆圈标记角点。圆圈的半径和厚度分别为 5 和 1。显示标记后的图像.
```python
max_corners = 50
min_distance = 0.5
block_size = 10
corners = cv2.goodFeaturesToTrack(equalized_image, max_corners, 0.01, min_distance, blockSize=block_size)
corners = np.intp(corners)

marked_image = resized_image.copy()
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(marked_image, (x, y), 5, (0, 0, 255), 1)  

plt.imshow(cv2.cvtColor(marked_image, cv2.COLOR_BGR2RGB))
plt.show()
```

