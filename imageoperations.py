import cv2

img = cv2.imread('messi5.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

r, g, b = cv2.split(img)
img = cv2.merge((r, g, b))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()