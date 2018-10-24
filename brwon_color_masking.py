#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/shijo/venv2/img3.JPG')
img = cv2.resize(img, (400, 300)); 
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (60,10,325,260)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]




hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img1 = cv2.resize(img, (430, 320)); 
hsv1 = cv2.resize(hsv, (430, 320)); 
cv2.imshow('orginal_img',img1);    #orginal image


def nothing(x):
    mask = cv2.inRange(hsv,(r,g,b), (30,255,255)) 
    
    cv2.imshow("brown", mask)  #show binary image

    
cv2.namedWindow('brown')   #creates window
"""creates a trackbar(slider name, window to be displayed, threshold min, threshold max, 
   callback function which is executed everytime trackbar value changes)"""
cv2.createTrackbar("red :", "brown", 0, 100, nothing);
cv2.createTrackbar("green:", "brown", 0, 150, nothing);
cv2.createTrackbar("blue :", "brown", 0, 150, nothing);

    
#while loop to update the threshold value 'thresh'
while(1):
    k = cv2.waitKey(1) & 0xFF;
    if k == 27:
        break;
    r = cv2.getTrackbarPos('red :', 'brown');
    g = cv2.getTrackbarPos('green :', 'brown');
    b = cv2.getTrackbarPos('blue :', 'brown');#gets current trackbar value
    #each time trachbar is changed the nothing func is called from the cv2.createTrackbar()
    
#END BINARISING & THRESHOLD SLIDER CODE :)



#keyboard binding function
k = cv2.waitKey(0);   
if k == 27:           #wait for ESC key to exit
    cv2.destroyAllWindows();  



# In[ ]:


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/shijo/venv2/img2.JPG')
img = cv2.resize(img, (400, 300)); 
plt.imshow(img) 
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (60,10,325,260)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

#plt.imshow(img)
plt.colorbar()
plt.show()


# In[ ]:





# In[ ]:




