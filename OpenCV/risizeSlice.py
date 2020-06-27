import cv2

img = cv2.imread("exemplo.jpg",1)
imgresize = img[::2,::2]
cv2.imwrite("exemplorisezeSlice.jpg",imgresize)
cv2.imshow("j1",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
