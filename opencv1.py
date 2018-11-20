import numpy as np
import cv2


img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

#For Line
#cv2.line(img,(line starting co-ordinates),(line ending co-ordinates),color(bgr value),line thickness)

cv2.line(img,(0,0),(150,150),(150,255,200),5)

#For Rectangle
#cv2.rectangle(img,(x1,x2 co-ordinates),(y1,y2 co-ordinates),color(bgr value),line thickness)

cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)

#For Rectangle
#cv2.rectangle(img,(centre co-ordinates),radius,color(bgr value),line thickness)
#for filled in circle line thickness will be -1

cv2.circle(img,(15,25),30,(0,150,255),15)
cv2.circle(img,(150,25),30,(0,15,200),-1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
