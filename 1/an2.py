# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:03
# @Author  : dong xin
# @File    : an2.py
# @Software: PyCharm
# 将图像灰度

import cv2
import numpy as np

def COLOR2GRAY(img):
    # height width channel color
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    out = 0.0722 * b + 0.7152 * g + 0.2126 * r
    out = out.astype(np.uint8)
    return out

if __name__ == '__main__':
    img = cv2.imread("../imori.jpg")
    img = COLOR2GRAY(img)
    cv2.imwrite("out2.jpg", img)