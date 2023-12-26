import cv2
import numpy as np



img = np.empty((300,300,3), np.uint8)

for row in range(300):
    for col in range(300):
        img[row, col] = [np.random.randint(0, 255),np.random.randint(0, 255),np.random.randint(0, 255)]

cv2.imshow('pic', img)
cv2.waitKey(0)

print(img.shape)