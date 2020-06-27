import cv2

img = cv2.imread("exemplo.jpg",1)
largura = img.shape[1]
altura = img.shape[0]
proporcao = float(altura/largura)
lnova = 600
anova = int(lnova*proporcao)
tnovo = (lnova,anova)
imgresize = cv2.resize(img,tnovo,interpolation = cv2.INTER_AREA)
cv2.imwrite("exemploriseze.jpg",imgresize)
cv2.imshow("j1",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
