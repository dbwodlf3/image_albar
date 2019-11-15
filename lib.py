import numpy as np

#해당 점의 시작점과 끝점을 알아야함. 같이 반환하자.

## Export Function

# inpurt canny image
def paintItemY(img):
    width = getItemSizeY(img)
    pass

## Image Slice

##Helper Function
def tourAtoB(pointA, pointB):
    #pointA[0] to pointB[0] x 좌표
    #pointA[1] to pointB[1] y 좌표.
    #pointA[0] < pointB[0] 이고, pointA[1] > pointB[1] 이어야함.
    for i in range(pointA[0], pointB[0]+1):
        for j in range(pointB[1], pointA[1]+1):
            print(i,j)

def paintRed(img, points):
    for i in (points):
         
        img[0][0] = (255, 255, 255)
    return img

def getItemSizeY(img):
    #get y size

    interval = 10
    before = 0
    item = [0]
    resultY = []

    startEndFlag = True
    length = 0
    start = (0,0)
    end = (0,0)
    resultPoint = []

    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if img[i][j] >1:
                if(item[-1] - j < interval):
                    if(startEndFlag):
                        start = (i, j)
                        startEndFlag = False
                    ## 점 사이의 간격이 Interval 보다 작다면 Item에 해당 점의 y 좌표를 추가.
                    item.append(j)
                    continue
                #선의 점이 10개가 이상이면 result에 등록.
                if(len(item)>10):
                    resultY.append(len(item))
                    length = len(item)
                    end = (i, j)
                    resultPoint.append((start,end,length))
                
                ## 점 사이의 간격이 Interval 보다 크다면 Item을 초기화
                item = [j]
                ## 점의 y좌표가 초기화 되므로 flag를 True로 바꾼다.
                startEndFlag = True
        print(i)
    #이제 어떤 녀석이 제일 큰 것인지 리턴. 반한되는 값에 + 50 값의 범위까지.
    return (resultY, resultPoint)

def getItemSizeX(img):
    #get y size

    interval = 10
    before = 0
    item = [0]
    resultX = []

    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if img[j][i] >1:
                if(item[-1] - j < interval):
                    ## 점 사이의 간격이 Interval 보다 작다면 Item에 해당 점의 y 좌표를 추가.
                    item.append(j)
                    continue
                #선의 점이 10개가 이상이면 result에 등록.
                if(len(item)>10):
                    resultX.append(len(item))
                
                ## 점 사이의 간격이 Interval 보다 크다면 Item에 해당 점의 y 좌표를 초기화.
                item = [j]
        print(i)
    #이제 어떤 녀석이 제일 큰 것인지 리턴. 반한되는 값에 + 50 값의 범위까지.
    return getFrequencyMax(resultX)

def getFrequencyMax(data):
    bins = np.arange(0,1050,50)
    result = np.histogram(data,bins)[0]
    resultCopy = result.copy()
    for i in range(1,len(result)-1):
        result[i] = result[i] + resultCopy[i-1]/2 + resultCopy[i+1]/2
    t =  list(result)
    print(list(bins))
    print(list(result))
    print(list(resultCopy))
    return bins[t.index(max(result))]