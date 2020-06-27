import numpy as np
import PIL
import cv2
import pyttsx3

wcam = cv2.VideoCapture(0)
hz = 20

while True:
    validation, frame =wcam.read()
    frame = cv2.flip(frame,1)
    (b,g,r) = cv2.split(frame)
    imgVazia = np.zeros((frame.shape[0],frame.shape[1]),dtype = "uint8")
    r = cv2.merge([imgVazia,imgVazia,r])
    g = cv2.merge([imgVazia,g,imgVazia])
    b = cv2.merge([b,imgVazia,imgVazia])
    cv2.imshow("frame",frame)
    cv2.waitKey(hz)
    cv2.imshow("frame",r)
    cv2.waitKey(hz)
    cv2.imshow("frame",g)
    cv2.waitKey(hz)
    cv2.imshow("frame",b)
    if (cv2.waitKey(hz) & 0xFF == ord('p')):
        break
    

wcam.release()
cv2.destroyAllWindows()
engine = pyttsx3.init()
engine.say("Prazer Marcos Matheus")
engine.runAndWait()