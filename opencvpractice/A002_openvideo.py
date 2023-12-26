import cv2
from cv2 import VideoCapture



########################  VideoCapture(0) can capture your current camera  #############################
cap = VideoCapture(0)

### cap a video
#cap = VideoCapture('./opencvpractice/vid.mov')

'''
ret returns boolean val to determine if u have next frame,
frame is like a pic, WaitKey(1) to show normal speed of vid,
resize frame = resize vid,
ord('q') means tap q to escape program
'''


while True:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
        cv2.imshow('vid', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break