# Importando biblioteca OpenCV
import cv2

# Lendo a imagem "entrada.jpeg" com imread()
# A imagem eh lida e armazenada na variavel img,
# a imagem eh armazenada como um objeto atraves de uma matriz de 3 dimensoes,
# cada dimensao possui um valor associado a uma das cores RGB.
# Caso a imagem seja grayscale (preto e branco), tera apenas 2 dimensoes na matriz.
img = cv2.imread('..\entrada.jpeg') 


# A funcao shape() retorna uma tupla contendo tres elementos,
# O primeiro elemento eh o valor da largua da imagem,
# O segundo elemento eh o valor da altura da imagem,
# O terceiro elemento eh a quantidade de canais que a imagem possui
print('Largura em pixels: ', end='')
print(img.shape[1]) # Imprime a largura da imagem no console
print('Altura em pixels: ', end='')
print(img.shape[0]) # Imprime a altura da imagem no console
print('Qtde de canais: ', end='')
print(img.shape[2]) # Imprime a Quantidade de Canais da imagem

cv2.imshow('Janela Imagem', img) # Exibe a Imagem em uma nova janela
cv2.waitKey(0) # Espera o usuario pressionar alguma tecla


cv2.imwrite("saida.jpg", img) # Salva a imagem no disco com o nome saida.jpg