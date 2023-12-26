import cv2
import numpy as np

img = np.zeros((400,400,3), np.uint8)



cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (255,0,0), 2)
cv2.rectangle(img, (100,100), (300,300), (123,234,12), cv2.FILLED)


#  your pic var, center, radius, color, thickness 
cv2.circle(img, (200,200), 50, (12,123,234), 4)


# your pic var, text, start point, font, textsize, color, thickness 
cv2.putText(img, 'Hello', (20, 370), cv2.FONT_ITALIC, 2, (245,113,11), 7)

cv2.imshow('drawing', img)
cv2.waitKey(0)