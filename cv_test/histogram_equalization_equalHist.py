import cv2 as cv
from matplotlib import pyplot as plt


def equalHist_demo(image):
	# 将图片变成灰度图
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    # 全局直方图均衡函数
    dst = cv.equalizeHist(gray)
    plt.subplot(1, 4, 3)
    plt.xlim([0, 256])
    plt.ylim([0, 4000])
    plt.grid(color='r', linestyle='--', linewidth=0.5, alpha=0.3)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title("equalHist_demo")
    cv.imshow("equalHist_demo", dst)

def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    plt.subplot(1,4,2)
    plt.hist(gray.ravel(), 256, [0,256])
    plt.title("gray")
    plt.xlim([0, 256])
    plt.ylim([0, 4000])
    plt.grid(color='r', linestyle='--', linewidth=0.5, alpha=0.3)
    # 局部直方图均衡化 对比度大小设置为5 处理块大小为8*8
    calhe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
    dst = calhe.apply(gray)
    plt.subplot(1, 4, 4)
    plt.grid(color='r', linestyle='--', linewidth=0.5, alpha=0.3)
    plt.hist(dst.ravel(), 256, [0, 256])
    plt.title("clahe_demo")
    plt.xlim([0, 256])
    plt.ylim([0, 4000])
    cv.imshow("clahe_demo", dst)


src = cv.imread("./imgs/17.bmp")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# 创建画图区域 figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
# num:图像编号或名称，数字为编号 ，字符串为名称
# figsize：figsize:指定figure的宽和高，单位为英寸
# dpi：指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80，1英寸等于2.5cm,A4纸是 21*30cm的纸张
# facecolor:背景颜色     edgecolor:边框颜色      frameon:是否显示边框
plt.figure("scenery",figsize=(12, 5))
# .subplot()创建子图
plt.subplot(1,4,1)
# 给子图加上网格
plt.grid(color='r', linestyle='--', linewidth=0.5, alpha=0.3)
# 绘制直方图
plt.hist(src.ravel(), 256, [0, 256])
plt.title("original picture")
plt.xlim([0,256])
plt.ylim([0,4000])
equalHist_demo(src)
clahe_demo(src)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
