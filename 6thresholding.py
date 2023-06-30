import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) #cv.threshold(function used to apply the thresholding) = img, threshold, max value, type of threshold 

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()

# thresholding form of simplification of image/visual data for analysis
# (simple thresholding) if pixel value < threshold, it is set to 0, else it is set to a max value
# adaptive thresholding - algorithm determines threshold for a pixel based on small region around it = different thresholds for different regions for same image