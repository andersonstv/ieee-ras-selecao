# Esse codigo realiza o reconhecimento de numeros a partir da posicao dos dedos
# da  mao em uma imagem. 

# Importando bibliotecas
import cv2 # OpenCV - Para processamento de imagens e ferramentas de visao computacional
import numpy as np # NumPy - Para realizar operacoes matematicas sobre arrays e matrizes, como a matriz representando a imagem lida pelo OpenCV
import mediapipe as mp # Mediapipe - Para realizar a deteccao de landmarks das maos para reconhecimento dos gestos
from mediapipe import Timestamp
from visualize_hands import draw_landmarks_on_image 

# Permite reajustar o tamanho da janela de exibicao do OpenCV
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

# Caminho para o modelo do MediaPipe
model_path = "hand_landmarker.task"


BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))


base_options = BaseOptions(model_asset_path=model_path)

# Define o modo de visao como Imagem
running_mode = VisionRunningMode.LIVE_STREAM

options = HandLandmarkerOptions(
    base_options=base_options,
    running_mode=running_mode,
    result_callback=print_result)

landmarker = HandLandmarker.create_from_options(options)

# Acessando captura de video da camera
capture = cv2.VideoCapture(0)
# Cria um loop para continuamente capturar o frame mais recente recebido da camera
while(1):
    ret, frame = capture.read()
    cv_timestamp = capture.get(cv2.CAP_PROP_POS_MSEC) / 1000
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    landmarker.detect_async(mp_image, cv_timestamp)

    cv2.imshow("Video", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()  