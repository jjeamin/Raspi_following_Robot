# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:06:35 2019

@author: JM
"""

import cv2
cap = cv2.VideoCapture(1)
ret, frame = cap.read()
cv2.imwrite('test.jpg', frame)
cap.release()