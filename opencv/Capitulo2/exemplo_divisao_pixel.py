# Importando biblioteca OpenCV
import cv2
# Lendo a imagem entrada.jpg
img = cv2.imread('..\entrada.jpeg') 

for y in range(0, img.shape[0]): # Percorre todas as linhas da matriz da imagem
    for x in range(0, img.shape[1]): # Percorre todas as colunas da matriz da imagem
        img[y, x] = (x%256,y%256,x%256) # substitui o valor do pixel pelo resultado da operacao Modulo por 256 de seus valores BGR

        
# Exibe a Imagem alterada e espera o usuario apertar uma tecla
cv2.imshow("Imagem modificada", img)
cv2.waitKey(0)