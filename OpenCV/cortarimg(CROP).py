import cv2

img = cv2.imread("dc.jpg",1)
crop = img[20:192,20:192]
cv2.imshow("Imagem",crop)
cv2.imwrite("imgcortada.jpg",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
