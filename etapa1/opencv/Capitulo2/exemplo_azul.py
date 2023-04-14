# Importando biblioteca OpenCV
import cv2
# Lendo a imagem entrada.jpg
img = cv2.imread('..\entrada.jpeg') 

for y in range(0, img.shape[0]): # Percorre todas as linhas da matriz da imagem
    for x in range(0, img.shape[1]): # Percorre todas as colunas da matriz da imagem
        img[y, x] = (255,0,0) # substitui o valor do pixel pela cor azul, (255, 0, 0) em BGR


# Exibe a Imagem apos substituir os pixels por azul 
cv2.imshow("Imagem modificada", img)
cv2.waitKey(0) # Espera o usuario pressionar alguma tecla
cv2.imwrite("output/azul.jpg", img)