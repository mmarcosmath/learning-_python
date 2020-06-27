import cv2
import numpy as np

img = np.zeros((500,500,3),dtype="uint8")
cv2.imshow("Imagem",img)
#img = cv2.merge()
for x in range(0,img.shape[0]):
    img[x:,x:] = (255%(x+1),0,0)
cv2.imshow("Imagem",img)
cv2.imwrite("imgCriada.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
