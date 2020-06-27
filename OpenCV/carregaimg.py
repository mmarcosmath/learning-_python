import cv2

img = cv2.imread("dc.jpg",1)# 1 para colorida 0 para BW
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
