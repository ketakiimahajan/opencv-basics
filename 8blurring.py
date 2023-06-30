import cv2
import numpy as np

#blurring and smoothing to get rid of noise
#niose = degradation in image signal (grainy image)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    lower_red = np.array([60, 35, 140])
    upper_red = np.array([180, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel = np.ones((15,15), np.float32)/225 
        #averaging block of pixels
        #np.ones = returns a new array of given shape and type filled with ones; creating multi-D array
        #np.float32 = computer no. format, occupies 32 bits on computer; each value in numpy array would be float of size 32
        
    smoothed = cv2.filter2D(res, -1, kernel)
    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()