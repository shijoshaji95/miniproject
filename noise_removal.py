#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

img = cv2.imread('/home/shijo/venv2/img3.JPG',1)
cv2.imshow('org_img', img)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('erosion', erosion) 

dilation = cv2.dilate(erosion,kernel,iterations = 1)
cv2.imshow('Dilation', dilation)

opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)



k = cv2.waitKey(0);   
if k == 27:           #wait for ESC key to exit
    cv2.destroyAllWindows();  


# In[ ]:




