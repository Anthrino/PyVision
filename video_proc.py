import cv2
import numpy as np

# Capture data from webcam
# vstream = cv2.VideoCapture(0)

vstream = cv2.VideoCapture('data/vid1.mp4')

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:
	ret, frame = vstream.read()
	cv2.imshow('frame', frame)

	if cv2.waitKey(1000) & 0xFF == ord('q'):
		break

vstream.release()
cv2.destroyAllWindows()