import lib as t
import numpy as np
import cv2

image = cv2.imread("shapes.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray_image, 50, 200)

cv2.imshow("canny",canny)
cv2.waitKey(0)

#test code

a,b = t.getItemSizeY(canny)

print(b)