<<<<<<< HEAD
import numpy as np
import cv2
import motor as m
import time

def move(rect):
    (x,y,w,h) = rect
    
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:01:09 2019

@author: JM
"""

import numpy as np
import cv2
import time
'''
#rectangle 컬러
red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
white = (255,255,255)
yellow = (0,255,255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)
'''

def make_1080p():
    cam.set(3, 1920)
    cam.set(4, 1080)

def make_240p():
    cam.set(3, 320)
    cam.set(4, 240)

def make_480p():
    cam.set(3, 640)
    cam.set(4, 480)

def change_res(width, height):
    cam.set(3, width)
    cam.set(4, height)
    
#480x640xpercent 
def rescale_frame(img, percent=75):
    width = int(img.shape[1] * percent/ 100)
    height = int(img.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation =cv2.INTER_AREA)
 
def move(rect):
    
    #ㅁ : 거리
    #ㅇ : 위치
    
    
    (x,y,w,h) = rect
    
    #center = (160,120)
>>>>>>> d6396411b0f01c0edf7b81e11141814e21bd962a
    center = (320,240)
    rect_center = (x+w//2, y+h//2)
    
    cv2.circle(img, center, 1, (0, 0, 255), 2);
    cv2.circle(img, rect_center, 1, (0, 0, 255), 2);
    
<<<<<<< HEAD
    go_back = -1 
    right_left = -1 
    
    if w*h > 45000 or y < 50:
        go_back = 2
    elif w*h < 35000 or y > 430:
=======
     #0 : 멈춤   1: 앞      2: 뒤
    go_back = -1
    #0 : 멈춤   1: 오른쪽  2: 뒤
    right_left = -1 
    
    
    # go,back,stop
    if w*h > 50000 or y < 50:
        go_back = 2
    elif w*h < 40000 or y > 430:
>>>>>>> d6396411b0f01c0edf7b81e11141814e21bd962a
        go_back = 1
    else:
        go_back = 0
      
<<<<<<< HEAD
    
    if rect_center[0] > center[0]+100:
        right_left = 1
    elif rect_center[0] < center[0]-100:
        right_left = 2
=======
       
    # right,left,stop
    if rect_center[0] > center[0]+100:
        right_left = 2
    elif rect_center[0] < center[0]-100:
        right_left = 1
>>>>>>> d6396411b0f01c0edf7b81e11141814e21bd962a
    else:
        right_left = 0
        
    #(right_left,go_back)
    location = (('stop','go','back'),
            ('left','go_left','back_left'),
            ('right','go_right','back_right'))    
    
<<<<<<< HEAD
    loc = location[right_left][go_back] 
    
    if loc == 'stop':
        m.stop()
        #m.setServo(1)
    elif loc == 'go':
        m.go()
        #m.setServo(2)
    elif loc == 'back':
        m.back()
        #m.setServo(3)
    elif loc == 'left':
        m.left()
        #m.setServo(4)
    elif loc == 'right':
        m.right()
        #m.setServo(5)
    elif loc == 'go_left':
        m.left()
        #m.setServo(6)
    elif loc == 'go_right':
        m.right()
        #m.setServo(7)
    elif loc == 'back_left':
        m.left()
        #m.setServo(8)
    elif loc == 'back_right':
        m.right()
        #m.setServo(9)
       
    print(loc)
	
    
 
=======
    print(location[right_left][go_back])
     
>>>>>>> d6396411b0f01c0edf7b81e11141814e21bd962a

def detectAndDisply(img,cascade):
    detector = cascade.detectMultiScale(img)
    
    max_size = -1
    index = 0
    
<<<<<<< HEAD
    #e1 = cv2.getTickCount()
    if(len(detector) != 0):
=======
    if(len(detector) != 0):
        #만약 검출된 얼굴이 1개 이상일 때
        #최댓값 하나로만 인식
        e1 = cv2.getTickCount()
>>>>>>> d6396411b0f01c0edf7b81e11141814e21bd962a
        for (x,y,w,h) in detector:
            if w*h > max_size:
                max_size = w*h
                max_pos = index
            index += 1
        
<<<<<<< HEAD
        max_rect = detector[max_pos]
        (max_x,max_y,max_w,max_h) = detector[max_pos]
        
        cv2.rectangle(img,(max_x,max_y),(max_x + max_w,max_y + max_h),(0,255,0),2)
    
        #e2 = cv2.getTickCount()

        #print(e2-e1)
        move(detector[max_pos])

    cv2.imshow('img',img)
    

#cascade = cv2.CascadeClassifier('./haar/haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier('./haar/lbpcascade_frontalface_improved.xml')

cam = cv2.VideoCapture(-1)

cam.set(320,240)

while 1:
    ret, img = cam.read()
    
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    time.sleep(0.1)    
    if ret:
        detectAndDisply(img,cascade)
        
        if cv2.waitKey(1) & 0xFF == 27:
            m.clean()
            break
            
    else:
        m.clean()
=======
        e2 = cv2.getTickCount()
        
        max_rect = detector[max_pos]
        
        (max_x,max_y,max_w,max_h) = detector[max_pos]
        
        cv2.rectangle(img,(max_x,max_y),(max_x + max_w,max_y + max_h),(0,255,0),2)
        
        print(e2-e1)
        #move(max_rect)

    cv2.imshow('img',img)


#학습된 파일
cascade = cv2.CascadeClassifier('C:/Users/JM/Git_store/humanfollow/haar/haarcascade_frontalface_default.xml')

#Cam ON
cam = cv2.VideoCapture(0)

make_240p()

while 1:
    #캠 정보 640x480
    ret, img = cam.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #Cam START
    if ret:
        detectAndDisply(img,cascade)
        
        #ESC Click -> EXIT
        if cv2.waitKey(1) & 0xFF == 27:
            break
            
    else:
>>>>>>> d6396411b0f01c0edf7b81e11141814e21bd962a
        print('no cam')
        break

            
cam.release()
<<<<<<< HEAD
cv2.destroyAllWindows()
=======
cv2.destroyAllWindows()
>>>>>>> d6396411b0f01c0edf7b81e11141814e21bd962a
