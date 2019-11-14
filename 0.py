import cv2
import numpy as np

'''
이미지 불러오기
'''

## img read
origin_img = cv2.imread("shapes.jpg")

copy_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)

## code

canny = cv2.Canny(copy_img, 50, 100)

## img show

# cv2.imshow("canny", canny)

# cv2.waitKey(0)

## save img
cv2.imwrite('test.jpg', canny)

## test code

temp = cv2.rectangle(origin_img, (0, 0), (100, 100), (0, 255, 0))


print(copy_img[0][0])

print()

def split() :
    pass