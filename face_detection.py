import cv2
import os

face_cascade = cv2.CascadeClassifier('DATA\haarcascades\haarcascade_frontalface_default.xml')

def displaay(img):
    while True:
        cv2.imshow('deteced_image',img)
        c = cv2.waitKey(1)
        if c ==27:
            break
    cv2.destroyAllWindows()

def detect_face(img):

    face_img = img.copy()
    blur_part = img.copy()

    rectangle_points = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=10)

    for (x,y,w,h) in rectangle_points:
         cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,255,0),2)
        # blur_part = blur_part[y:y+h,x:x+w]
        # blur_roi = cv2.medianBlur(blur_part,7)
        # face_img[y:y+h,x:x+w] = blur_roi
    return  face_img


"""Face detection in an Image"""

img = cv2.imread('image source/namaskara.jpg')
detected_img = detect_face(img)

detected_img = cv2.resize(detected_img,(0,0),detected_img,0.3,0.3)
displaay(detected_img)




"""live web cam face detection"""
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret,frame = cap.read(0)
#     frame = detect_face(frame)
#
#     cv2.imshow('face_detect',frame)
#
#     c = cv2.waitKey(1)
#     if c == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

"""face detection in an video"""
# cap = cv2.VideoCapture(r'C:\Users\vs6993\Desktop\appa birthday\VID_20190728_180302.mp4')
#
# if cap.isOpened() == False :
#     print("video not fund")
#
# while cap.isOpened():
#     ret,frame = cap.read()
#     if ret == True:
#         frame = detect_face(frame)
#
#         cv2.imshow('face_detect',frame)
#
#         c = cv2.waitKey(0)
#         if c == 27:
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()
