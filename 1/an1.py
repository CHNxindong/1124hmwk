# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 8:58
# @Author  : dong xin
# @File    : an1.py
# @Software: PyCharm
# 读取图像，然后将BGR通道替换成RGB通道

import cv2

# 题目应该出错了， 是BGR到RGB 因为imread 是BGR
def BGR2RGB(img):
    # height width channel color
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    # 换颜色赋值
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b
    return img

if __name__ == '__main__':
    img = cv2.imread("../imori.jpg")
    img = BGR2RGB(img)
    cv2.imwrite("out1.jpg", img)