import cv2

#rgb
# na tupla é bgr
img = cv2.imread("dc.jpg",1)# 1 para colorida 0 para BW
img[range(0,img.shape[0]),range(0,img.shape[1])] = (0,0,0)

cv2.imshow("img",img)
cv2.waitKey(0)
#img[0:img.shape[0],0:img.shape[1]] = (255,0,0) #pinta toda a imagem
#cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
