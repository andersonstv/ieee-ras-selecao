# Importando biblioteca OpenCV
import cv2
# Lendo a img entrada.jpg
img = cv2.imread('..\entrada.jpeg') 

for y in range(0, img.shape[0], 1): # percorre as linhas
    for x in range(0, img.shape[1], 1): # percorre as colunas
        img[y, x] = (0,(x*y)%256,0) # substitui o pixel por um valor BGR com vermelho e azul zerados, e o valor de verde para o resultado de (x*y)

# Exibe a Imagem alterada e espera o usuario apertar uma tecla
cv2.imshow("img modificada", img)
cv2.waitKey(0)
cv2.imwrite("output/verde_tons.jpg", img)