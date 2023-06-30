import cv2
import numpy as np

# reducing bg by detecting motion
# extracts the moving fg from the static bg; use this to compare two similar images, and extract differences between them

cap = cv2.VideoCapture('people-walking.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2() # initializing subtractor

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame) # applying on each frame
    
    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)
    
    if cv2.waitKey(30) & 0xFF == ord('m'):
        break
    
cap.release()
cv2.destroyAllWindows()

# finds changes from previous frames and notes as fg while rest is bg to be removed