# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:33
# @Author  : dong xin
# @File    : an9.py
# @Software: PyCharm

import cv2
import numpy as np

# ？？？？？？？？？？？？？？
def gaussian_filter(img, K_size=3, sigma=1.3):
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    # 加padding ********************************
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)

    # ??????? K怎么来的
    K = np.zeros((K_size, K_size), dtype=np.float)
    for x in range(-pad, -pad + K_size):
        for y in range(-pad, -pad + K_size):
            K[y + pad, x + pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    K /= (2 * np.pi * sigma * sigma)
    K /= K.sum()
    print(16 * K)

    tmp = out.copy()

    for y in range(H):
        for x in range(W):
            for c in range(C):
                # 滤波： 按位相乘 求和 ？是求和后每位一样， 还是就一个值：就一个值 x，y在动
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

if __name__ == '__main__':
    img = cv2.imread("imori_noise.jpg")
    # 高斯滤波 由sima 变半径
    out = gaussian_filter(img, K_size=3, sigma=1.3)
    cv2.imwrite("out9.jpg", out)