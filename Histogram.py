#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np, cv2

# 처음 그림에서 드래그를 하여 네모를 그림.
# 이후 네모에 해당하는 부분에 대한 히스토그램 출력
# ESC 누를 시 프로세스 종료


# In[7]:


def draw_histo(hist, shape = (200, 256)) :
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0]
    
    for i, h in enumerate(hist) :
        x = int(round(i * gap))
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)


# In[8]:


def draw_rectangle(event, x, y, flags, param):
    global x1,y1, click                                     # 전역변수 사용

    if event == cv2.EVENT_LBUTTONDOWN:                      # 마우스를 누른 상태
        click = True 
        x1, y1 = x,y

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;                                      # 마우스를 때면 상태 변경
        cv2.rectangle(img,(x1,y1),(x,y),(1,1,1), 3)
        
        cut = img[x1:x, y1:y]
        hist = cv2.calcHist([cut], [0], None, [32], [0, 256])
        hist_img = draw_histo(hist)
        
        cv2.imshow('image', img) 
        cv2.imshow("hist_img", hist_img)


# In[9]:


click = False   
x1,y1 = -1,-1

img= cv2.imread("images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)               

while True:
    cv2.imshow('image', img)    

    k = cv2.waitKey(1) & 0xFF   
        
    if k == 27:               
        break
        
cv2.destroyAllWindows()

