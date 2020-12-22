from skimage.measure import compare_ssim

import cv2


image1 = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\barcode1.jpg")
image2 = cv2.imread(r"C:\Users\vs6993\PycharmProjects\Open_CV\DATA\barcode2.jpg")

grayA = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))
