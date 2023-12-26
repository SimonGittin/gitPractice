import cv2

img = cv2.imread('shape.png')

imgContour = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 200, 250)
contours, hierachy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:

    # chosen pic, contour, -1 means print all contour, color, thickness
    cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4)

    '''
    print(cv2.contourArea(cnt))

    # chosen contours, closed or not
    print(cv2.arcLength(cnt, True)) 
    '''

    if cv2.contourArea(cnt) > 500:
        length = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, length*0.02, True)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)

        corners = len(vertices)
        if corners == 3:
            cv2.putText(imgContour, 'Triangle', (x, y-5), cv2.FONT_ITALIC, 1, (0, 0, 255), 1)
        elif corners == 4:
            cv2.putText(imgContour, 'Rectangle', (x, y-5), cv2.FONT_ITALIC, 1, (0, 0, 255), 1)
        elif corners == 5:
            cv2.putText(imgContour, 'Pentagon', (x, y-5), cv2.FONT_ITALIC, 1, (0, 0, 255), 1)

cv2.imshow('Contour', canny)
cv2.imshow('Contoured', imgContour)



cv2.waitKey(0)
