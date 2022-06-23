#!/usr/bin/env python 

import cv2

#video_capture = cv2.VideoCapture(0)
video_capture = cv2.VideoCapture("rosfolder_udemy/ros_essentials/src/topic03_perception/video/ros.mp4")
while(True):
	ret, frame = video_capture.read()
	
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = cv2.resize(frame, (100,00), fx=0.5,fy=0.75) # fx is the scale factor along the X-axis, fy is the scale factor along the Y-axis .(100,0 ) is the size of the frame.
	#cv2.line(frame,(0,0),(511,511),(255,0,0),5)
	cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()