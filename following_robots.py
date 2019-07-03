from imutils.video import WebcamVideoStream
from imutils.video import FPS
import imutils
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
        right_left = 2
    elif rect_center[0] < center[0]-100:
        right_left = 1
    else:
        right_left = 0
        
    location = (('stop','go','back'),
            ('left','go_left','back_left'),
            ('right','go_right','back_right'))    
    loc = location[right_left][go_back] 

    if loc == 'stop':
        m.stop()
    elif loc == 'go':
        m.go()
    elif loc == 'back':
        m.back()
    elif loc == 'left':
        m.left()
    elif loc == 'right':
        m.right()
    elif loc == 'go_left':
        m.go_left()
    elif loc == 'go_right':
        m.go_right()
    elif loc == 'back_left':
        m.back_left()
    elif loc == 'back_right':
        m.back_right()  
    print(loc)

def detectAndDisply(img,cascade):
    detector = cascade.detectMultiScale(img)
    
    max_size = -1
    index = 0
    
    if(len(detector) != 0):
        for (x,y,w,h) in detector:
            if w*h > max_size:
                max_size = w*h
                max_pos = index
            index += 1

        max_rect = detector[max_pos]
        (max_x,max_y,max_w,max_h) = detector[max_pos]
        
        cv2.rectangle(img,(max_x,max_y),(max_x + max_w,max_y + max_h),(0,255,0),2)

        move(detector[max_pos])

    cv2.imshow('img',img)
    

#cascade = cv2.CascadeClassifier('./cascade_xml/haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier('./cascade_xml/lbpcascade_frontalface_improved.xml')

#cam = cv2.VideoCapture(-1)

cam = WebcamVideoStream(src=-1).start()
pre = 0

while 1:
    #ret, img = cam.read()
    img = cam.read()
    #img = imutils.resize(img,height=400)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #fps
    cur = time.time()
    sec = cur - pre
    pre = cur

    fps = 1/sec

    cv2.putText(img,"FPS : "+str(fps),(100,100),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),2)

    #Cam START
    #if ret:
    detectAndDisply(img,cascade)
        
    #ESC Click -> EXIT
    if cv2.waitKey(1) & 0xFF == 27:
        m.clean()
        break
    #else:
        #print('no cam')
        #break

            
#cam.release()
cv2.destroyAllWindows()
cam.stop()
