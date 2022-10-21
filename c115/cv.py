import cv2
import numpy as np
img=cv2.imread("3333333.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]
text="i love coding"
cv2.putText(img,text,(20,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0))
cv2.imshow("poster",img)


cv2.waitKey(0)