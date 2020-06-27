import cv2

#rgb
# na tupla é bgr
img = cv2.imread("dc.jpg",1)# 1 para colorida 0 para BW

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        img[i,j] = (0,(i*j)%256,0)

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
