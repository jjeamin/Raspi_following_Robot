import numpy as np
import cv2
import motor as m
import time

def move(rect):
    (x,y,w,h) = rect
    
    center = (320,240)
    rect_center = (x+w//2, y+h//2)
    
    cv2.circle(img, center, 1, (0, 0, 255), 2);
    cv2.circle(img, rect_center, 1, (0, 0, 255), 2);
    
    go_back = -1 
    right_left = -1 
    
    if w*h > 45000 or y < 50:
        go_back = 2
    elif w*h < 35000 or y > 430:
        go_back = 1
    else:
        go_back = 0
      
    
    if rect_center[0] > center[0]+100:
        right_left = 1
    elif rect_center[0] < center[0]-100:
        right_left = 2
    else:
        right_left = 0
        
    #(right_left,go_back)
    location = (('stop','go','back'),
            ('left','go_left','back_left'),
            ('right','go_right','back_right'))    
    
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
	
    
 

def detectAndDisply(img,cascade):
    detector = cascade.detectMultiScale(img)
    
    max_size = -1
    index = 0
    
    #e1 = cv2.getTickCount()
    if(len(detector) != 0):
        for (x,y,w,h) in detector:
            if w*h > max_size:
                max_size = w*h
                max_pos = index
            index += 1
        
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
        print('no cam')
        break

            
cam.release()
cv2.destroyAllWindows()
