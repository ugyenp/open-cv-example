import numpy as np;
import cv2

img1 = np.zeros((768, 1024, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('white.jpg')
dimension = img2.shape

print('size', dimension)

bitAnd = cv2.bitwise_and(img2, img1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitAnd', bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()
