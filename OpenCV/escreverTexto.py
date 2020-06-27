import numpy as np
import cv2
imagem = cv2.imread('img.jpg')
fonte = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagem,'OpenCV',(15,65), fonte,
1,(0,0,0),1,cv2.LINE_AA)
cv2.imshow("Ponte", imagem)
cv2.imwrite("escrevi.jpg",imagem)
cv2.waitKey(0)
