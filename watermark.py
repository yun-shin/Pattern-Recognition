#!/usr/bin/env python
# coding: utf-8

# In[52]:


import numpy as np, cv2


# In[53]:


background = cv2.imread("images/bit_test.jpg")
watermark  = cv2.imread("images/logo.jpg")

w = int(input("가로에 들어갈 개수를 입력하시오."))
h = int(input("가로에 들어갈 개수를 입력하시오."))

W = background.shape[1] // w
H = background.shape[0] // h

logo_plt = np.zeros((background.shape[0], background.shape[1], 3), background.dtype)

resized_watermark = cv2.resize(watermark, (W,H))

for i in range(h):
    for j in range(w):
        logo_plt[H*i:H*(i+1), W*j:W*(j+1)] = resized_watermark


# In[54]:


masks = cv2.threshold(logo_plt, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H, W),(h, w) = background.shape[:2], logo_plt.shape[:2]
x, y = (W - w) // 2, (H - h) // 2
roi = background[y:y+h, x:x+w]

fore = cv2.bitwise_and(logo_plt, logo_plt, mask=fg_pass_mask)
back = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

dst = cv2.add(back, fore)

cv2.imshow('dst', dst)
cv2.waitKey()

