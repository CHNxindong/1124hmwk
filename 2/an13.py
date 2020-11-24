# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:25
# @Author  : dong xin
# @File    : an13.py
# @Software: PyCharm

import cv2
import numpy as np

def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)

    return out

def max_min_filter(img, K_size=3):
    H, W = img.shape
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
    tmp = out.copy()
    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x] = np.max(tmp[y: y + K_size, x: x + K_size]) - \
                np.min(tmp[y: y + K_size, x: x + K_size])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

if __name__ == '__main__':
    img = cv2.imread("../imori.jpg").astype(np.float)
    gray = BGR2GRAY(img)
    out = max_min_filter(gray, K_size=3)
    cv2.imwrite("out13.jpg", out)
