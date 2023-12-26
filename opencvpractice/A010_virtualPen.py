import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 215, 102])
    upper = np.array([3, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    findContour(mask)

    cv2.imshow('Result', result)

def findContour(img):
    contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4)
        if cv2.contourArea(cnt) > 500:
            length = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, length*0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)

while True:
    ret, frame = cap.read()
    if ret == True:
        imgContour = frame.copy()
        frame = cv2.resize(frame, (0,0), fx = 1, fy = 1)
        cv2.imshow('vid', frame)
        cv2.imshow('Contour',imgContour)
        findPen(frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break