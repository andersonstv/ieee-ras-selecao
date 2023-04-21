# Esse codigo realiza o reconhecimento de numeros a partir da posicao dos dedos
# da  mao em uma imagem. Utilizando as bilbioteca OpenCV e Numpy, junto com o framework 
# de visao computacional MediaPipe

# Importando bibliotecas
import cv2 # OpenCV - Para processamento de imagens e ferramentas de visao computacional
import numpy as np # NumPy - Para realizar operacoes matematicas sobre arrays e matrizes, como a matriz representando a imagem lida pelo OpenCV
import mediapipe as mp # Mediapipe - Para realizar a deteccao de landmarks das maos para reconhecimento dos gestos
from visualize_hands import draw_landmarks_on_image 

# Caminho para o modelo do MediaPipe, O modelo Hand Landmarker permite 
# realizar deteccao de maos em uma imagem e identificar caracteristicas como
# qual mao (esquerda ou direita) esta na imagem, posicoes de landmarks na mao
# como as articulacoes, punho e ponta dos dedos
model_path = "hand_landmarker.task"

# Importa classes do Mediapipe para realizar a configuracao do Hand Landmark
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Cria um objeto do tipo BaseOptions com o caminho para o modelo
base_options = BaseOptions(model_asset_path=model_path)

# Define o modo de visao do Landmarker como IMAGE. Isso significa
# que o Landmarker ira lidar com imagens estaticas.
running_mode = VisionRunningMode.IMAGE

# Cria um objeto contendo informaceos das opcoes escolhidas para o Hand Landmarker
options = HandLandmarkerOptions(
    base_options=base_options,
    running_mode=running_mode)

# Inicializa um detector de maos, landmarker, a partir das opcoes selecionadas.
landmarker = HandLandmarker.create_from_options(options)

# Le uma imagem de entrada, uma fotografia contendo uma mao representando um numero
img = mp.Image.create_from_file("hand-sample-images\\left_2.jpeg")

# Realiza a deteccao de maos na imagem com o landmarker e armazena os resultados em uma variavel
landmark_result = landmarker.detect(img)

# Gera uma versao da imagem de entrada, com anotacoes do landmarker sobrepostas sobre a imagem
annotated_image = draw_landmarks_on_image(img.numpy_view(), landmark_result)

# Converte a imagem do MediaPipe para o formato do OpenCV
annotated_image_cv = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)

# Configuracao que permite reajustar o tamanho da janela de exibicao do OpenCV
cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)

# Imprime os resultados do landmarker no console
print(landmark_result)

# Exibe a imagem resultante
cv2.imshow("Imagem", annotated_image_cv)
cv2.waitKey(0)