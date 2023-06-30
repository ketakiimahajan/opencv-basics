import cv2
import numpy as np

# detecting corners 

img = cv2.imread('13corner.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # detecting corners goodFeaturesToTrack function
corners = np.intp(corners) #int0?

for corner in corners: # iterating each corner to make a circle around around point which is corner
    x, y = corner.ravel() # ravel = changes 2D/multi-D array to contigous flattened array
    cv2.circle(img, (x,y), 3, 255, -1)
    
cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
