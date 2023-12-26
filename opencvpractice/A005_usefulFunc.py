'''
gray the pic
blur
find the outlines
thicken the outline
thin the outline
'''

##########################################################################




import cv2
import numpy as np

img = cv2.imread('./opencvpractice/cat.jpg')

img = cv2.resize(img, (0,0), fx = 1.5, fy = 1.5)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(img, (5,5), 5)
canny_img = cv2.Canny(img, 100, 150)                                    #find the lines
dilate_img = cv2.dilate(img, np.ones((10,10), np.uint8), iterations=2)  #thick the lines
erode_img = cv2.erode(img, np.ones((10,10), np.uint8), iterations=2)    #unthick the lines


cv2.imshow('image', img)
cv2.imshow('grayed image', gray_img)
cv2.imshow('blurred image', blur_img)
cv2.imshow('edged image', canny_img)
cv2.imshow('dilated image', dilate_img)
cv2.imshow('eroded image', erode_img)

cv2.waitKey(0)