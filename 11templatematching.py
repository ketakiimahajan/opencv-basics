import cv2
import numpy as np

# finding identical regions of main image that match given template using threshold

img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg',0)
w, h = template.shape[::-1]
    # [::-1] = inverts array, if 1234 --> 4321 because image gets inverted in R/L during cv2.imread = coor are messed up for matchTemplate

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) #match template method for searching & finding location of template in main
threshold = 0.7 # 0.7 means match should be 80% of template and main img; if you reduce = more false positives
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for pt in zip(*loc[::-1]) = for points with values > threshold; zip is container of all such points and it will iterate to all such points and draw rectangle around it