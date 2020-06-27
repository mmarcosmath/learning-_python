import cv2

wcam = cv2.VideoCapture(0)

while True:
    validation, frame =wcam.read()
    cv2.imshow("frame",frame)
    if (cv2.waitKey(1) & 0xFF == ord('p')):
        break

wcam.release() 
cv2.destroyAllWindows()
