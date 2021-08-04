import cv2
import numpy as np

filenames = './imgs/73.bmp'
img = cv2.imread(filenames)
# 将图片高和宽分别赋值给x，y
x, y = img.shape[0:2]
cv2.imshow('orginal', cv2.resize(img, (int(y / 2), int(x / 2))))

#laplace处理
laplace = cv2.Laplacian(img,cv2.CV_16S,ksize=3)
#转回uint8
img = cv2.convertScaleAbs(laplace)

x, y = img.shape[0:2]
cv2.imshow('sobelimg', cv2.resize(img, (int(y / 2), int(x / 2))))
cv2.waitKey(0)
cv2.destroyAllWindows()