# Esse codigo escurece as bordas superior e inferior da imagem

# Importando biblioteca OpenCV
import cv2
# Lendo a imagem entrada.jpg
img = cv2.imread('..\entrada.jpeg') 

for y in range(0, img.shape[0]): # Percorre todas as linhas da matriz da imagem
    for x in range(0, img.shape[1]): # Percorre todas as colunas da matriz da imagem
            (b, g, r) = img[y, x] 
            factor = abs(img.shape[0]/2 - y) # calcula um fator de "shading" baseado na distancia ate o centro da imagem
            new_b = max(0, b - factor)
            new_g = max(0, g - factor)
            new_r = max(0, r - factor)
            img[y, x] = (new_b, new_g, new_r)


# Exibe a Imagem apos substituir os pixels por azul 
cv2.imshow("Imagem modificada", img)
cv2.waitKey(0) # Espera o usuario pressionar alguma tecla