import numpy as np

def getFrequencyMax(data, bins):
    result = data.copy()
    for i in range(1,len(result)-1):
        result[i] = round(result[i] + data[i-1]/2 + data[i+1]/2)
    return bins[result.index(max(result))]

test_data =[285, 116, 89, 79, 108, 158, 330, 509, 564, 415, 153, 61, 35, 21, 6, 3, 4, 2, 2, 1]
bins = np.arange(0,1050,50)

print(getFrequencyMax(test_data, bins))