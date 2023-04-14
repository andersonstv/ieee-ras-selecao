# Esse codigo substitui todos os pixels em que sua posicao (x, y) eh divisivel por 3 pela cor vermelha

# Importando biblioteca OpenCV
import cv2
# Lendo a imagem entrada.jpg
img = cv2.imread('..\entrada.jpeg') 

for y in range(0, img.shape[0]): # Percorre todas as linhas da matriz da imagem
    for x in range(0, img.shape[1]): # Percorre todas as colunas da matriz da imagem
        if(y%3 == 0 and x%3 == 0): 
            img[y, x] = (0,0,255)


# Exibe a Imagem apos substituir os pixels por azul 
cv2.imshow("Imagem modificada", img)
cv2.waitKey(0) # Espera o usuario pressionar alguma tecla
cv2.imwrite("output/div3.jpg", img)