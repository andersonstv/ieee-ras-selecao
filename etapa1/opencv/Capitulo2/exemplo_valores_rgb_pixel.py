# Importando biblioteca OpenCV
import cv2
# Lendo a imagem entrada.jpg
img = cv2.imread('..\entrada.jpeg') 

# Obtendo os valores das cores do primeiro pixel da imagem [0, 0]
# b = azul
# g = verde
# r = vermelho
# por motivos de implementacao, o OpenCV utiliza na ordem BGR
(b, g, r) = img[0, 0] 

# Exibindo os valores do primeiro pixel
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)