import numpy as np

def getItemSizeY(img):
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
    #이제 어떤 녀석이 제일 큰 것인지 리턴. 반한되는 값에 + 50 값의 범위까지.
    return getFrequencyMax(resultY)

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
    #이제 어떤 녀석이 제일 큰 것인지 리턴. 반한되는 값에 + 50 값의 범위까지.
    return getFrequencyMax(resultX)

def getFrequencyMax(data):
    result = data.copy()
    bins = np.arange(0,1050,50)
    for i in range(1,len(result)-1):
        result[i] = round(result[i] + data[i-1]/2 + data[i+1]/2)
    return bins[result.index(max(result))]