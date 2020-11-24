# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:36
# @Author  : dong xin
# @File    : an10.py
# @Software: PyCharm

import cv2
import numpy as np

def median_filter(img, K_size=3):
    H, W, C = img.shape

    pad = K_size // 2
    out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
    out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)
    tmp = out.copy()

    for y in range(H):
        for x in range(W):
            for c in range(C):
                # 找到3*3 的median 就一个值   ：都是一个值替代3*3
                out[pad+y, pad+x, c] = np.median(tmp[y:y+K_size, x:x+K_size, c])
    out = out[pad:pad+H, pad:pad+W].astype(np.uint8)
    return out

if __name__ == '__main__':
    img = cv2.imread("imori_noise.jpg")
    out = median_filter(img, K_size=3)
    cv2.imwrite("out10.jpg", out)