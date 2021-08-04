import cv2 as cv
from matplotlib import pyplot as plt


# 对于plt.title(“中文”)，不能再图一些标题显示中文，则在程序前加上以下两行代码即可：
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
image = cv.imread("sine.jpg")
cv.imshow("original picture", image)
plt.figure("图")
plt.subplot(2,2,1)
plt.title("原图直方图")
plt.hist(image.ravel(), 256, [0, 256])
color = ["b", "g", "r"]
plt.subplot(2,2,3)
plt.title("原图三通道直方图")
for i, color in enumerate(color):
    hist = cv.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color = color)
# 分离每一个通道
b, g, r = cv.split(image)
# 创建局部直方图均衡化
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))
# 对每一个通道进行局部直方图均衡化
b = clahe.apply(b)
g = clahe.apply(g)
r = clahe.apply(r)
# 合并处理后的三通道 成为处理后的图
image = cv.merge([b, g, r])
color = ["b", "g", "r"]
plt.subplot(2,2,4)
plt.title("三通道直方图均衡化")
for i, color in enumerate(color):
    hist = cv.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color = color)
plt.subplot(2,2,2)
plt.title("直方图均衡化")
plt.hist(image.ravel(), 256, [0, 256])
cv.imshow("clahe", image)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
