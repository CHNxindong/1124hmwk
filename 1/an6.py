# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 9:14
# @Author  : dong xin
# @File    : an6.py
# @Software: PyCharm

import cv2

# def COMPRESSBUS(img):
#     # height width channel color
#     b = img[:, :, 0].copy()
#     g = img[:, :, 1].copy()
#     r = img[:, :, 2].copy()
#     # 换颜色赋值
#     img[:, :, 0] = COMPRESSCOLOR(b)
#     img[:, :, 1] = COMPRESSCOLOR(g)
#     img[:, :, 2] = COMPRESSCOLOR(r)
#     return img
#
# def COMPRESSCOLOR(img):
#     img[img>= 0 and img < 64] = 32
#     img[img >= 64 and img < 128] = 96
#     img[img >= 128 and img < 192] = 160
#     img[img >= 192 and img < 256] = 224
#     return img

# ????????????????????????????? 到底像素， 通道 怎么获取与 comput
def COMPRESSBUS(img):
	out = img.copy()
	out = out // 64 * 64 + 32
	return out

if __name__ == '__main__':
    img = cv2.imread("../imori.jpg")
    img = COMPRESSBUS(img)
    cv2.imwrite("out6.jpg", img)