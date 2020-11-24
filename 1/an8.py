# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:31
# @Author  : dong xin
# @File    : an8.py
# @Software: PyCharm

import cv2

import numpy as np

# 平均池化：这段代码是借用的
# ******************** 池化和 卷积网络都不是一定会改变大小， 只是变模糊， 大小由 步长
def average_pooling(img, G=8):
    out = img.copy()

    # 因为是每个通道计算， 所以要先拿到 SHAPE
    H, W, C = img.shape
    Nh = int(H / G)
    Nw = int(W / G)

    for y in range(Nh):
        for x in range(Nw):
            for c in range(C):
                # 每个通道选G*G，不同通道
                out[G * y:G * (y + 1), G * x:G * (x + 1), c] = np.max(
                    out[G * y:G * (y + 1), G * x:G * (x + 1), c]).astype(np.int)

    return out

if __name__ == '__main__':
    img = cv2.imread("../imori.jpg")
    img = average_pooling(img)
    cv2.imwrite("out8.jpg", img)