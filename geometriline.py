import cv2
import numpy as np

# img = cv2.imread('testimg.jpg', 1)
img = np.zeros([700, 700, 3], np.uint8)
img = cv2.line(img, (0,0), (255, 255), (255, 0, 0), 2 )
img = cv2.arrowedLine(img, (0,0), (255, 255), (0, 255, 0), 2)
img = cv2.rectangle(img, (300, 0), (500, 128), (0, 0, 255), -1)
img = cv2.circle(img, (600, 34), 34, (255, 0, 0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Open Cv', (10,500), font, 4, (255, 0, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()

elif k == ord(s):
    cv2.imwrite('geoimg.png', img)



