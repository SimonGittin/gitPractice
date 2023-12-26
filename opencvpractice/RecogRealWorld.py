import cv2

cap = cv2.VideoCapture(0)


def face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    path = 'face_detect.xml'

    faceCascade = cv2.CascadeClassifier(path)
    face_rect = faceCascade.detectMultiScale(gray, 1.1, 3)

    for x, y, w, h in face_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)


while True:
    ret, frame = cap.read()
    face(frame)
    if ret == True:
        frame = cv2.resize(frame, (0,0), fx = 1, fy = 1)
        cv2.imshow('vid', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break