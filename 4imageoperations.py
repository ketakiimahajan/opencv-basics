import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255, 255, 255] #changing pixel 
px = img[55, 55] #acessing px value by row & col coordinates
#print(px) #output shows value of pixel

img[100:150, 100:150] = [255, 255, 255] #changing color of an area (range of pixels)

watch_face = img[37:111, 107:194] #region of image, roi
img[0:74, 0:87] = watch_face #111-74, 194-107

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
