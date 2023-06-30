import cv2
import numpy as np

#removing white noise using morphological transformations

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    lower_red = np.array([60, 35, 140])
    upper_red = np.array([180, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel = np.ones((5,5), np.uint8) # 8 bit unsigned integer type
    erosion = cv2.erode(mask, kernel, iterations = 1)
        # erodes boundries of foreground objects; kernel slides through img; in original img pixel = 0/1; only 1 if all pixels under kernel = 1 else made to 0; 
        # pixels near boundry removed/ size of objects decreases/ useful for removing small white noises
    
    dilation = cv2.dilate(mask, kernel, iterations = 1 )
        # opposite of erosion; pixel element is 1 if atleast one pixel under kernel = 1; increases size of obeject
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # remove false positives i.e. removing noises in bg
    
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        # remove false negatives i.e. removing black pixels in the object
    
    # tophat = difference between input image and opening of the image
    # blackhat = difference between the closing of the input image and input image
    
    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()