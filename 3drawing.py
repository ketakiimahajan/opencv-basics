import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255, 255, 255), 15) #drawing line(where to draw, starting pos, ending pos, color(bgr), width)

cv2.rectangle(img, (15,25), (200,150), (0, 255, 0), 5) #drawing rectangle

cv2.circle(img, (100,63), 55, (0,0, 255), -1) #drawing circle(, , , , fill(-1))

pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32 ) #array of coordinates 
pts = pts.reshape(-1, 1, 2) #reshapes array to 1x2??
cv2.polylines(img, [pts], False, (0, 255, 255), 5) #cv2.polylines (to draw line)(, array of coordinates...)

font = cv2.FONT_HERSHEY_SIMPLEX #specifying font
cv2.putText(img, 'OpenCV', (0,130), font, 1, (200, 255, 255), 2, cv2.LINE_AA) #adding text

cv2.imshow('image', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
