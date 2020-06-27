import cv2

#rgb
# na tupla é bgr

img = cv2.imread("dc.jpg",1)# 1 para colorida 0 para BW
img[0:img.shape[0]//2,0:img.shape[1]//2] = (0,0,0) #pinta um quadrado, usando o metodo slice

cv2.imshow("img",img)
cv2.waitKey(0)
#img[0:img.shape[0],0:img.shape[1]] = (255,0,0) #pinta toda a imagem
#cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
