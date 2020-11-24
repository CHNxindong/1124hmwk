# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:25
# @Author  : dong xin
# @File    : an12.py
# @Software: PyCharm

import cv2
import numpy as np

def motion_filter(img, K_size=3):
    H, W, C = img.shape

    K = np.diag([1] * K_size).astype(np.float)
    print(K)
    K /= K_size

    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
    tmp = out.copy()

    for y in range(H):
        for x in range(W):
            for c in range(C):
                # 按位相乘 求和 一个值替代 3*3
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

if __name__ == '__main__':
    img = cv2.imread("imori.jpg")
    out = motion_filter(img, K_size=3)
    cv2.imwrite("out12.jpg", out)
