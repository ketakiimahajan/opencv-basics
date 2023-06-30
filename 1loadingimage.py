import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading image
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE) #if not specified, coloured image is read and alpha channel is reduced (opaqueness)

""" img = cv2.imread('watcg.jpg', cv2.1) 
    IMREAD_COLOR = 1
    IMREAD_UNCHANGED = -1
    IMREAD_GRAYSCALE = 0 etc. """

#cv2.imshow('image', img) #shows image
#cv2.waitKey(0) #waits for any key to be pressed
#cv2.destroyAllWindows() #close everything

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') #cmap = colormap; bicubic is one of the methods of interpolation e.g. bilinear, nearest neighbor
plt.plot([50, 100], [80,100], 'c', linewidth = 5)
plt.show()
