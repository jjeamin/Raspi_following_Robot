import cv2

cam = cv2.VideoCapture(0)

while(True):
	ret, frame = cam.read()
	cv2.imshow('image',frame)
	
	k = cv2.waitKey(10) & 0xFF
	if k == 27:
		break

cam.release()
cv2.destroyAllWindows()
