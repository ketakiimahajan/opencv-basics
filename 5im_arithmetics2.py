import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

rows, cols, channels = img2.shape #shape() gives dimensions of the image like height(0), width(1) and channels(2) of the image
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #converting img2
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) 

#cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1) 
cv2.waitKey(0)
cv2.destroyAllWindows()