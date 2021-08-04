#批量修改文件名
#批量修改图片文件名
import os
import re
import sys
def renameall():
    # 待修改文件夹
    fileList = os.listdir(r"E:\Users\raychiu\Desktop\工业缺陷检测项目集\瓶盖缺陷检测\dataset\temp")
    # 输出文件夹中包含的文件
    print("修改前："+str(fileList))
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(r"E:\Users\raychiu\Desktop\工业缺陷检测项目集\瓶盖缺陷检测\dataset\temp")
    # 名称变量
    num = 196
    # 遍历文件夹中所有文件
    for fileName in fileList:
        # 匹配文件名正则表达式 .+表示多个任意字符，\.表示.，即匹配*****.bmp（后缀为.bmp的文件）
        pat = ".+\.(jpg|png|gif|bmp)"
        # 进行匹配
        pattern = re.findall(pat, fileName)
        # 文件重新命名
        os.rename(fileName, (str(num)+'.'+pattern[0]))
        # 改变编号，继续下一项
        num = num+1
    print("---------------------------------------------------")
    # 改回程序运行前的工作目录
    os.chdir(currentpath)
    # 刷新
    sys.stdin.flush()
    # 输出修改后文件夹中包含的文件
    print("修改后："+str(os.listdir(r"E:\Users\raychiu\Desktop\工业缺陷检测项目集\瓶盖缺陷检测\dataset\temp")))

renameall()