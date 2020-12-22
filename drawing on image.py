import cv2
import numpy as np
import random

def circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        colour= random.randrange(100,250)
        cv2.circle(img,(x,y),25,(0,colour,0),1)
        print(x,y)

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',circle)

img = np.zeros((512,512,3))
while True:
    cv2.imshow("my_drawing", img)

    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()
