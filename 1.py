import cv2
import numpy as np

data = [4, 0,1,2,3,4,5,6,7,8,9]
bins = np.arange(0,15,5)

hist, bins2 = np.histogram(data, bins)

print(hist)
print(bins2)