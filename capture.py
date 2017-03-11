import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

web_cam = cv2.VideoCapture(0)
camera = PiCamera
rawCapture = PiRGBArray(camera)

# warm up camera
time.sleep(0.1)

while True:
	# ret, color = web_cam.read()
	#cv2.imwrite('/messigray.png',color)
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array

	print image
	cv2.waitKey(500)
