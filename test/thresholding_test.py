# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:33:37 2019

@author: JM
"""

import cv2

img = cv2.imread('road.jpg')

new_img = cv2.resize(img,(300,400),interpolation=cv2.INTER_AREA)
new_img_gray = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(new_img, 12, 255, cv2.THRESH_BINARY)
retval2, threshold2 = cv2.threshold(new_img_gray, 12, 255, cv2.THRESH_BINARY)

th = cv2.adaptiveThreshold(new_img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original',new_img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()