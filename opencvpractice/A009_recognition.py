import cv2

img = cv2.imread('iu.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

path = 'face_detect.xml'

faceCascade = cv2.CascadeClassifier(path)
face_rect = faceCascade.detectMultiScale(gray, 1.1, 3)

for x, y, w, h in face_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)

cv2.imshow('img', img)
cv2.waitKey(0)