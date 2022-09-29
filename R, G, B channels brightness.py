#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)

if image is None : raise Exception("영상 파일 읽기 오류")
if image.ndim != 3 : raise Exception("컬러 영상 아님")
    
bgr = cv2.split(image)

blue = np.zeros((image.shape[0],image.shape[1], 3), image.dtype)
green = np.zeros((image.shape[0],image.shape[1], 3), image.dtype)
red = np.zeros((image.shape[0],image.shape[1], 3), image.dtype)

for h in range(0, image.shape[0]) :
    for w in range(0, image.shape[1]) :       
        blue[h][w][0] = bgr[0][h][w]
        green[h][w][1] = bgr[1][h][w]
        red[h][w][2] = bgr[2][h][w]


cv2.imshow("image", image)
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

cv2.waitKey(0)

