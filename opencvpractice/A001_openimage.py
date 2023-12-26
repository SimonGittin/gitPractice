import cv2

img = cv2.imread('./opencvpractice/cat.jpg')



#resize picture
#img = cv2.resize(img,(100,100))
img = cv2.resize(img, (0,0), fx = 1.5, fy = 1.5)


#show pic
cv2.imshow('image', img)

cv2.waitKey(5000) # waitKey(0) equals infinite time, tap q to manually ends
