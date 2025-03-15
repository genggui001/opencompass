---
jupyter:
  title: Straight lines and circles detection
  module: opencv
  dataset: chess.png, board.png
  difficulty: Middle
  idx: 22
  num_steps: 6
  step_types:
    - exec
    - vis
    - vis
    - vis
    - vis
  modules: 
    - opencv 
    - opencv & matplotlib
    - opencv & matplotlib & numpy
    - opencv & matplotlib
    - opencv & matplotlib & numpy
---

File Path: 'data/chess.png', 'data/board.png'.

Load the chess image in gray scale.
```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('data/chess.png',0)
```

Apply the Canny edge detection algorithm to the image. The function requires three arguments: the image, the lower threshold, and the upper threshold. Here, we are using 50 as the lower threshold and 150 as the upper threshold. The aperture size is set to 3. Display the edge-detected image.
```python
edges = cv2.Canny(img,50,150,apertureSize = 3)
plt.imshow(edges, cmap='gray')
plt.show()
```

Apply the Hough Line Transform to the edge-detected image. Here, we use a resolution of 1 pixel and 1 radian (np.pi/180) and a threshold value of 200. Draw lines on the original image based on the results of the Hough Line Transform. Use a for loop to iterate over each line (represented by rho and theta values) in the lines array. Calculate the x and y coordinates of the two points that define each line and draw the line on the image. Display the image with the lines.
```python
import numpy as np
lines = cv2.HoughLines(edges,1,np.pi/180,200)
if lines is not None:
   for rho,theta in lines[0]:
       a = np.cos(theta)
       b = np.sin(theta)
       x0 = a*rho
       y0 = b*rho
       x1 = int(x0 + 1000*(-b))
       y1 = int(y0 + 1000*(a))
       x2 = int(x0 - 1000*(-b))
       y2 = int(y0 - 1000*(a))
       cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
plt.imshow(img)
plt.show()
```

Now, apply the Probabilistic Hough Line Transform to the edge-detected image. Here, we are using a resolution of 1 pixel and 1 radian (np.pi/180), a threshold value of 100, a minimum line length of 100, and a maximum gap of 10. Draw lines on the original image based on the results of the Probabilistic Hough Line Transform. Use a for loop to iterate over each line (represented by x1, y1, x2, y2 coordinates) in the lines array. Display the image with the lines.
```python
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
plt.imshow(img)
plt.show()
```

Load a board image from path in grayscale, apply a median blur of size 5 and then apply the Hough Circle Transform. Here, we are using the HOUGH_GRADIENT method, a 1:1 ratio, a minimum distance of 20 pixels, and a minimum and maximum radius of 0. Draw circles on the original image based on the results of the Hough Circle Transform. Use a for loop to iterate over each circle (represented by center coordinates and radius) in the circles array. Draw the circle on the image. If the thickness is set to a negative value, the circle will be filled. Display the image with the circles.
```python
img = cv2.imread('data/board.png',0)
img = cv2.medianBlur(img,5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
plt.imshow(img)
plt.show()
```