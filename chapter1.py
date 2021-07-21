import cv2
import  numpy as np
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(11,11),0)
imgCanny = cv2.Canny(img,150,200)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgErode = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("original_img", img)
cv2.imshow("gray_image",imgGray)
cv2.imshow("BLur_image",imgBlur)
cv2.imshow("Canny_img",imgCanny)
cv2.imshow("dilation_img",imgDilation)
cv2.imshow("erode_img",imgErode)
cv2.waitKey(0)

