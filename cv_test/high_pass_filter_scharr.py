import cv2
import numpy as np

filenames = './imgs/73.bmp'
img = cv2.imread(filenames)
# 将图片高和宽分别赋值给x，y
x, y = img.shape[0:2]
cv2.imshow('orginal', cv2.resize(img, (int(y / 2), int(x / 2))))

#scharr处理 基本和Sobel算子一样，只是没有了超参数ksize,使用固定的3*3ksize。
imgx = cv2.Scharr(img,cv2.CV_16S,1,0)
imgy = cv2.Scharr(img,cv2.CV_16S,0,1)
# 转回uint8
imgx_uint8 = cv2.convertScaleAbs(imgx)
imgy_uint8 = cv2.convertScaleAbs(imgy)
# x,y方向组合
img = cv2.addWeighted(imgx_uint8, 0.5, imgy_uint8, 0.5, 0)

x, y = img.shape[0:2]
cv2.imshow('sobelimg', cv2.resize(img, (int(y / 2), int(x / 2))))
cv2.waitKey(0)
cv2.destroyAllWindows()