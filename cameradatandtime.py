import cv2
import datetime

captureVideo = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# captureVideo.set(1, 3000)
# captureVideo.set(2, 3000)

resolutionheight = captureVideo.get(1)
resolutionWidth = captureVideo.get(2)

while captureVideo.isOpened:
    returnedBooleanValue, videoFrames = captureVideo.read()

    if returnedBooleanValue == True: 
        font = cv2.FONT_HERSHEY_SIMPLEX
        tdate = str(datetime.datetime.now())
        text = 'Height:' + str(resolutionheight) + ' ' + 'Width:' + str(resolutionWidth)
        videoFrames = cv2.putText(videoFrames, tdate, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('colored_image', videoFrames)

        waitKey = cv2.waitKey(1)
        exitKey = ord('q')
        if waitKey ==  exitKey:
            break
    
    else:
        break

captureVideo.release()
cv2.destroyAllWindows()
