# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:32:47 2019

@author: JM
"""
import numpy as np
import cv2

img = cv2.imread('11.jpg',cv2.IMREAD_COLOR)

#line, rectangle
cv2.line(img,(0,0),(200,300),(255,255,255),50)
cv2.rectangle(img,(10,15),(100,100),(0,0,255),15)
cv2.circle(img,(15,15), 63, (0,255,0), -1)

pts = np.array([[0,0],[10,10],[20,30],[100,0]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()