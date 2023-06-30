import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

#add = img1 + img2
#add = cv2.add(img1, img2) #built-in addition operation; not ideal as img is very bright(max 255)

#addweighted function helps in  transition of the image to another (blend), different weights are given to give a feeling of blending or transparency
weighted = cv2.addWeighted(img1, 0.6, img2, 0,4, 0) #parameters = first img, the weight, second img, the weight, gamma(measurement of light)

cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

