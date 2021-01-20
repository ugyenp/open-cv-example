import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(3, 1208)
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

while cap.isOpened():

    ret, frames = cap.read()
    if ret == True: 

        gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)

        if cv2.waitKey(1) == ord(q):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()
