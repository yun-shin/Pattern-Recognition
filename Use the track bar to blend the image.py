#!/usr/bin/env python
# coding: utf-8

# In[24]:


import cv2
import numpy as np

win_name = 'Alpha blending'     # 창 이름
trackbar_name = 'fade'          # 트렉바 이름

def onChange(x):
    alpha = cv2.getTrackbarPos('image1', win_name) / 100
    beta = cv2.getTrackbarPos('image2', win_name) / 100
    
    dst = cv2.addWeighted(image1, alpha, image2, beta, 0) 
    addh = np.hstack((image1, dst, image2))
    
    cv2.imshow(win_name, addh)


image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
dst = np.zeros((image1.shape[0], image1.shape[1]), image1.dtype)
addh = np.hstack((image1, dst, image2))

cv2.imshow(win_name, addh)

cv2.createTrackbar('image1', win_name, 0, 100, onChange)
cv2.createTrackbar('image2', win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()

