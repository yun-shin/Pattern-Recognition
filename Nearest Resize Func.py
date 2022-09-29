#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np, cv2

def my_resize(logo, dsize, fx = 0.0, fy = 0.0) :
    
    if dsize == (0, 0) :
        image = np.zeros((int(logo.shape[0]*fy),int(logo.shape[1]*fx), 3), logo.dtype)

    else :
        image = np.zeros((dsize[1], dsize[0], 3), logo.dtype)
        fx = image.shape[1] / logo.shape[1]
        fy = image.shape[0] / logo.shape[0]

    for h in range(0, image.shape[0]) :
        for w in range(0, image.shape[1]) :
            image[h][w] = logo[int(h/fy)][int(w/fx)]
    
    return image


# In[20]:


image = cv2.imread("images/wirte_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("파일 에러")

img2 = cv2.resize(image, (0, 0), fx = 0.3, fy = 0.3, interpolation= cv2.INTER_LINEAR)
img3 = my_resize(image, (0, 0), fx = 0.3, fy = 0.3)

cv2.imshow("opencvresize", img2)
cv2.imshow("useresize", img3)

cv2.waitKey(0)


# In[ ]:




