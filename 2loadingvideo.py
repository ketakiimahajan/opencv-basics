import cv2
import numpy as np

cap = cv2.VideoCapture(0) #returns video frame by frame from e.g. webcam 1 or 'output.avi'

fourcc = cv2.VideoWriter_fourcc(*'XVID') #fourcc = used to compress frames; for MP4, fourcc specification = XVID
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True: #infinite loop
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting to gray

    out.write(frame)

    cv2.imshow('frame', frame) #imshow to display each frame
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('m'): #wait 1ms between frames; m to exit
        break

cap.release() #releases webcam and closes all imshow() windows

cv2.destroyAllWindows()
