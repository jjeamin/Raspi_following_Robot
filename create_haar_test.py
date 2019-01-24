# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:23:11 2019

@author: JM
"""

import numpy as np
import cv2

#this is the cascade we just made. Call what you want
cascade = cv2.CascadeClassifier('data/cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # add this
    # image, reject levels level weights.
    my_cascade = cascade.detectMultiScale(gray)
    
    # add this
    for (x,y,w,h) in my_cascade:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()