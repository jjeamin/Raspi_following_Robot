import cv2


face_cascade = cv2.CascadeClassifier('/home/pi/workspace/raspi-humanfollow/haar/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/workspace/raspi-humanfollow/haar/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
prevHeight = 320

while cap.isOpened():
	ret, img = cap.read()
	width,height,channels = img.shape
	
	if ret:
		cv2.imshow('camera',img)
		
		#ESC Click -> EXIT
		if cv2.waitKey(1) & 0xFF == 27:
			break
			
	else:
		print('no camera')
		break
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.3,5)
	
	
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

		
cap.release()
cv2.destroyAllWindows()


