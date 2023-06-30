import cv2
import numpy as np

# object detection with haar cascade 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # CascadeClassifier method in cv2 module supports loading of haar-cascade XML files
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # applying face detection on image using detectMultipleScale which returns boundry rect for detected faces

    for (x, y, w, h) in faces: # iterating through detected faces and drawing rectangles
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        roi_gray = gray[y:y+h, x:x+w] # defining roi for detected face to detect eyes within it
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray) # returns coordinates of boundry rect of eyes in (ex,ey,ew,eh) format
        
        for (ex, ey, ew, eh) in eyes: 
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),(0, 255, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(30) & 0xFF == ord('m'):
        break

cap.release()
cv2.destroyAllWindows()