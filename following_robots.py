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

def detectAndDisply(img,cascade,mode='human'):
    max_size = -1
    index = 0
    
	if mode == 'human':
		detector = cascade.detectMultiScale(img)
	
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
	
	elif mode == 'qr':
        	barcodes = pyzbar.decode(img)
		
		if(len(barcodes) != 0):
			for barcode in barcodes:
				(x,y,w,h) = barcode.rect
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
			move((x,y,w,h))
		else:
			m.stop()
			
    cv2.imshow('img',img)
    
def main(mode):
	if mode == 'human':
		#cascade = cv2.CascadeClassifier('./cascade_xml/haarcascade_frontalface_default.xml')
		cascade = cv2.CascadeClassifier('./cascade_xml/lbpcascade_frontalface_improved.xml')
	else:
		cascade = None
		
		
	cam = WebcamVideoStream(src=-1).start()
	prevTime = 0

	while 1:
		#ret, img = cam.read()
		img = cam.read()
		#img = imutils.resize(img,height=400)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
		#fps
		#현재 시간 가져오기 (초단위로 가져옴)
		curTime = time.time()

		#현재 시간에서 이전 시간을 빼면?
		#한번 돌아온 시간!!
		sec = curTime - prevTime
		#이전 시간을 현재시간으로 다시 저장시킴
		prevTime = curTime

		# 프레임 계산 한바퀴 돌아온 시간을 1초로 나누면 된다.
		# 1 / time per frame
		fps = 1/(sec)

		# 프레임 수를 문자열에 저장
		str = "FPS : %0.1f" % fps

		# 표시
		cv2.putText(img, str, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))

		#Cam START
		#if ret:
		detectAndDisply(img,cascade,mode)
			
		#ESC Click -> EXIT
		if cv2.waitKey(1) & 0xFF == 27:
			m.clean()
			break

				
	#cam.release()
	cv2.destroyAllWindows()
	cam.stop()
	
if __name__ == "__main__":
    mode = 'human'
    main(mode)
