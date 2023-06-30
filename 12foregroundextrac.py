import cv2
import numpy as np
import matplotlib.pyplot as plt

# find the fg & remove the bg

img = cv2.imread('12extraction.jpg')

#define mask
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64) #temp array of bg pixel
fgdModel = np.zeros((1, 65), np.float64)

#define rectange 
react = (161, 79, 150, 150) # x, y, w, h; draws a reactangle around the object to be considered as fg, rest is bg

cv2.grabCut(img, mask, react, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT) # grabcut = for fg extraction; v2.GC_INIT_WITH_RECT because rectangle mode is used; 5 = no. of iterations  

mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

img = img*mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()

""" pixels into 4 classes: 0=bg, 1=fg, 2=possible bg, 3=possible fg;
    if mask=2 or 0, then matrix is 0 else 1;
    this is multiplied by input img; 
"""