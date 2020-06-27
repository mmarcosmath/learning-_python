import cv2

#rgb
# na tupla é bgr
img = cv2.imread("dc.jpg",1)# 1 para colorida 0 para BW
print("",img.shape[1])

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if (i==j) and (i<(img.shape[0]/2)):
            img[i:i+10,j:j+10] = (255,0,0)
        if ((i+j)==img.shape[0]-1) and (i<(img.shape[0]/2)):
            img[i:i+10,j-10:j] = (255,0,0)
        if j == 0:
            img[i:i+10,j:j+10] = (255,0,0)
        if j == img.shape[1]-1:
            img[i-10:i+1,j-10:j+1] = (255,0,0)

cv2.imshow("img",img)
cv2.imwrite("fizumM.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
