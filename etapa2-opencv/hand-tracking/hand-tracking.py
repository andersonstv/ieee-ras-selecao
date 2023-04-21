# Esse codigo realiza o reconhecimento de numeros a partir da posicao dos dedos
# da  mao em uma imagem. 

# Importando bibliotecas
import cv2 # OpenCV - Para processamento de imagens e ferramentas de visao computacional
import numpy as np # NumPy - Para realizar operacoes matematicas sobre arrays e matrizes, como a matriz representando a imagem lida pelo OpenCV
import mediapipe as mp # Mediapipe - Para realizar a deteccao de landmarks das maos para reconhecimento dos gestos
from visualize_hands import draw_landmarks_on_image 

# Caminho para o modelo do MediaPipe
model_path = "hand_landmarker.task"

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

base_options = BaseOptions(model_asset_path=model_path)

# Define o modo de visao como Imagem
running_mode = VisionRunningMode.IMAGE

options = HandLandmarkerOptions(
    base_options=base_options,
    running_mode=running_mode)

landmarker = HandLandmarker.create_from_options(options)

img = mp.Image.create_from_file("hand-sample-images\\2.jpeg")
landmark_result = landmarker.detect(img)

annotated_image = draw_landmarks_on_image(img.numpy_view(), landmark_result)
annotated_image_cv = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)

# Permite reajustar o tamanho da janela de exibicao do OpenCV
cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)

# Exibe a imagem resultante
cv2.imshow("Imagem", annotated_image_cv)
cv2.waitKey(0)

# Acessando captura de video da camera
#capture = cv2.VideoCapture(0)

#while(1):
#    ret, frame = capture.read()
#    cv2.imshow("Video", frame)
#    k = cv2.waitKey(30) & 0xff
#    if k == 27:
#        break

#capture.release()
#cv2.destroyAllWindows()    