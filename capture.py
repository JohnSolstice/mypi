import cv2

web_cam = cv2.VideoCapture(0)

while True:
	ret, color = web_cam.read()
	#cv2.imwrite('/messigray.png',color)
	print color
	cv2.waitKey(500)
