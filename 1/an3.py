# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:08
# @Author  : dong xin
# @File    : an3.py
# @Software: PyCharm
# 将灰度的阈值设置为128来进行二值

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

def TOBINARY(out, threshodling):
    out[out < threshodling] = 0
    out[out >= threshodling] = 255
    return out

if __name__ == '__main__':
    img = cv2.imread("../imori.jpg")
    out = COLOR2GRAY(img)
    binimg = TOBINARY(out, 128)
    cv2.imwrite("out3.jpg", binimg)