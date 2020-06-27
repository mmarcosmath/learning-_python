import cv2

img = cv2.imread("simpmod.png",1)
#cv2.imshow("DiariodeClasse",img)
largura,altura = img.shape[1],img.shape[0]

print(altura)
print(largura)
b,g,r = img[25,25]
print(r,g,b)
i,j=0,0

while i<altura:
    
    j = 0
    while j<largura:
        
        b,g,r = img[i,j]
        #img[i:i+5,j:j+5] = (r%256,g%256,b%256)
        if ((r <50 and g <50) and b<50) :
            img[i,j] = (255,255,255)
        
        #if i==j:
         #   img[i,j] = (r%256,g%256,b%256)
        j = j + 1
    i = i + 1


    

cv2.imshow("img",img)
cv2.imwrite("simpmod.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##import cv2
##import numpy as np
##
##imagemCarregada = cv2.imread("exemplo.jpg", 0)
##
##cv2.imshow("ImagemCarregada", imagemCarregada)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
