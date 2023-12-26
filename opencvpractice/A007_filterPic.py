import cv2
import numpy as np

img = cv2.imread('./opencvpractice/XiWinnie.jpg')

#print(img.shape) -> (394, 700, 3)

def empty():
    pass

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 320)

cv2.createTrackbar('Hue Min', 'Trackbar', 0 , 179, empty)
cv2.createTrackbar('Hue Max', 'Trackbar', 179 , 179, empty)
cv2.createTrackbar('Sat Min', 'Trackbar', 0 , 255, empty)
cv2.createTrackbar('Sat Max', 'Trackbar', 255 , 255, empty)
cv2.createTrackbar('Val Min', 'Trackbar', 0 , 255, empty)
cv2.createTrackbar('Val Max', 'Trackbar', 255 , 255, empty)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    hue_min = cv2.getTrackbarPos('Hue Min', 'Trackbar')
    hue_max = cv2.getTrackbarPos('Hue Max', 'Trackbar')
    sat_min = cv2.getTrackbarPos('Sat Min', 'Trackbar')
    sat_max = cv2.getTrackbarPos('Sat Max', 'Trackbar')
    val_min = cv2.getTrackbarPos('Val Min', 'Trackbar')
    val_max = cv2.getTrackbarPos('Val Max', 'Trackbar')
    
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Xi', img)
    cv2.imshow('Xi hsv', hsv)
    cv2.imshow('Xi mask', mask)
    cv2.imshow('Xi result', result)

    cv2.waitKey(1)

