


import numpy as np
import cv2

img = cv2.imread('/home/shijo/venv2/img.JPG',0)              # Load an color image in grayscale
cv2.imshow('image',img)                                      #to display image
k = cv2.waitKey(0) & 0xFF                                    # wait for any key to press
if k == 27:                                                  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):                                          # wait for 's' key to save and exit
    cv2.imwrite('/home/shijo/venv2/messigray.png',img)       # to save the image
    cv2.destroyAllWindows()                                  # to exit

"""

    cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
    cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

"""
