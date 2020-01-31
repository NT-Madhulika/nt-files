import numpy as np 
import cv2 
  
# Creating a black image with 3 channels 
# RGB and unsigned int datatype 
img = np.zeros((1000, 600, 3), dtype = "uint8") 
img[:,0:1000//2] = (0,0,0)      # (B, G, R)
img[:,1000//2:500] = (0,0,0)
cv2.imshow('dark', img) 
  
# Allows us to see image 
# untill closed forcefully 
cv2.waitKey(0) 
cv2.destroyAllWindows()