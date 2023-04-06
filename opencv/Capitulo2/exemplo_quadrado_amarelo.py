# Importando biblioteca OpenCV
import cv2
# Lendo a img entrada.jpg
img = cv2.imread('..\entrada.jpeg') 

for y in range(0, img.shape[0], 10): # percorre linhas, pulando de 10 em 10
    for x in range(0, img.shape[1], 10): # percorre colunas, pulando de 10 em 10
        img[y:y+5, x: x+5] = (0,255,255) # Substitui os pixels em um quadrado de 5x5 pela cor amarela

# Exibe a Imagem alterada e espera o usuario apertar uma tecla
cv2.imshow("img modificada", img)
cv2.waitKey(0) 