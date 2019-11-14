import cv2
import numpy as np

'''
이미지 불러오기
'''


## helper Function
def getItemSize(img):
    #get y size

    interval = 10
    before = 0
    item = [0]

    resultY = []

    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if img[i][j] >1:
                if(item[-1] - j < interval):
                    ## 점 사이의 간격이 Interval 보다 작다면 Item에 해당 점의 y 좌표를 추가.
                    item.append(j)
                    continue
                #선의 점이 10개가 이상이면 result에 등록.
                if(len(item)>10):
                    resultY.append(len(item))
                
                ## 점 사이의 간격이 Interval 보다 크다면 Item에 해당 점의 y 좌표를 초기화.
                item = [j]
                print(i,j)
    #get x size

    return resultY

##test code

kernel = np.ones((5,5), np.uint8)

origin_img = cv2.imread("shapes.jpg")
gray_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray_img, 50, 100)
#dilation = cv2.dilate(canny, kernel, iterations = 1)
closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)


cv2.imwrite('test.jpg', closing)

print(len(canny))
print(canny[3023])

'''
for i in range(0, len(canny)):
    for j in range(0, len(canny[i])):
        if canny[i][j] >1:
            print(i,j,canny[i][j])
'''

test = getItemSize(canny)

bins = np.arange(0,1050, 50)

print(test)

a,b = np.histogram(test, bins)

print(a)
print(b)