import cv2

#rgb
# na tupla é bgr
img = cv2.imread("dc.jpg",1)# 1 para colorida 0 para BW

for i in range(0,img.shape[0],10):
    for j in range(0,img.shape[1],10):
        img[i:i+5,j:j+5] = (255,0,0) #i:i+5,j:j+5 significa dizer as alteraçoes ocorrerão de i ate i+1 assim como pra j

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
