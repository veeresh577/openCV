import cv2
import numpy as np

def diplay_img(img):
    while True:
        cv2.imshow("I am",img)

        if cv2.waitKey(1) & 0xFF == 27 : # waiting for i msec and closeing the image by Esc button
            break
    cv2.destroyAllWindows()

img = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\image source\ganga.jpg")
img = cv2.resize(img,(0,0),img,0.2,0.2)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,img = cv2.threshold(img,155,255,cv2.THRESH_BINARY)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,5)
# gama = .1
#
# img = np.power(img,gama)

diplay_img(img)

