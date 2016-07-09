#!/usr/bin/python                                                                                                                                                                  

import cv2

#cap = cv2.VideoCapture('3DDisplay.mov')                                                                                                                                           
cap = cv2.VideoCapture(0)

fcount = 0
count = 0
while (cap.isOpened()):
    ret, frame = cap.read()

    cv2.putText(frame, "w: %d | frame:%d" %(fcount, count), (100, 100), cv2.cv.CV_FONT_HERSHEY_PLAIN, 3, (100,0,250), 5)

    cv2.imshow('frame:%d' %(fcount), frame)
    fcount += 1
    count += 1
    if fcount > 3:
        fcount = 0

    if cv2.waitKey(250) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
