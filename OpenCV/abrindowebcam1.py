import numpy as np
import cv2
wcam = cv2.VideoCapture(0)

while True:
    validation, frame =wcam.read()
    fonte = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,'OpenCV',(15,65), fonte,
2,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow("frame",frame)
    if (cv2.waitKey(1) & 0xFF == ord('p')):
        break
    

wcam.release()
cv2.destroyAllWindows()
