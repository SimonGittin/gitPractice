import cv2

img = cv2.imread('cat.jpg')
img = cv2.resize(img, (0,0), fx = 2, fy = 2)

print(img.shape)

left_up_img = img[:224, :225]
right_bottom_img = img[224:448, 225:450]


cv2.imshow('image', img)
cv2.imshow('Left up img', left_up_img)
cv2.imshow('Right bottom img', right_bottom_img)



cv2.waitKey(0)

