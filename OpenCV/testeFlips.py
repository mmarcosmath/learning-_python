import cv2

img = cv2.imread("simp.png",1)
cv2.imshow("janela",img)
cv2.waitKey(0)
for x in range(-2,2):
    cv2.imshow("janela",cv2.flip(img,x))
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
