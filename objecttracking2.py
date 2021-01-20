import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('tracking')
cv.resizeWindow('tracking', 500, 300)

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

cv.createTrackbar('LH', 'tracking', 0, 255, nothing)
cv.createTrackbar('LS', 'tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'tracking', 0, 255, nothing)
cv.createTrackbar('UH', 'tracking', 255, 255, nothing)
cv.createTrackbar('US', 'tracking', 255, 255, nothing)
cv.createTrackbar('UV', 'tracking', 255, 255, nothing)

while True:
    _, frame = cap.read()
    width = 400
    height = 360
    dim = (width, height)
    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)

    hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)

    l_h = cv.getTrackbarPos('LH', 'tracking')
    l_s = cv.getTrackbarPos('LS', 'tracking')
    l_v = cv.getTrackbarPos('LV', 'tracking')

    u_h = cv.getTrackbarPos('UH', 'tracking')
    u_s = cv.getTrackbarPos('US', 'tracking')
    u_v = cv.getTrackbarPos('UV', 'tracking')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()