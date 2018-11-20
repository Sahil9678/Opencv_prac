import numpy as np 
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(20,20,20),12)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()