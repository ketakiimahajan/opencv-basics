import cv2
import numpy as np

#filtering for some specific color

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converts the BGR color space of image to HSV color space
    
    lower_red = np.array([60, 35, 140]) #sets lower and upper bounds for blue hue
    upper_red = np.array([180, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red) #creating mask for blue color
    res = cv2.bitwise_and(frame, frame, mask = mask)
    #black region in mask has value 0, when multiplied with original image, all non-blue regions is removed
    #mask=mask compares both frames and if both are same, values are separated (AND operator)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    if cv2.waitKey(30) & 0xFF == ord('m'):
        break
    
cv2.destroyAllWindows()
cap.release()