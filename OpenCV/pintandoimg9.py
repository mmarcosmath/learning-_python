import numpy as np
import cv2
imagem = cv2.imread('img.jpg')
vermelho = (0, 0, 0)
verde = (0, 255, 0)
azul = (255, 0, 0)
cv2.line(imagem, (0, 0), (100, 200), verde) #recebe 4 parametros 1= a img, 2=ponto inicial, 3=ponto final, 4 = cor (x,x,x)
cv2.line(imagem, (300, 200), (150, 150), vermelho, 5) #ultimo argumento é a qtd de pxl
cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)
(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
for raio in range(0, 175, 15):
    cv2.circle(imagem, (X, Y), raio, vermelho)
cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)
