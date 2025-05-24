import cv2
import torch
import numpy as np
import urllib.request
import os
import pathlib

# Corrigir caminhos se estiver usando Windows
pathlib.PosixPath = pathlib.WindowsPath

# Obter o diretório atual do script
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'best.pt')  # Caminho até o best.pt

# Verificar se o arquivo best.pt existe
if not os.path.exists(path):
    print(f"ERRO: Arquivo de pesos 'best.pt' não encontrado no caminho: {path}")
    exit(1)

# URL da câmera (troque pelo seu link se necessário)
image_url = 'http://192.168.0.35/cam-hi.jpg'

# Carregar o modelo
model = torch.hub.load('fase6/yolov5', 'custom', path=path_modelo, source='local')

model.conf = 0.2

print(f"Modelo carregado com sucesso de: {path}")

# Loop para capturar e detectar
while True:
    try:
        img_resp = urllib.request.urlopen(image_url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)

        results = model(im)

        # Exibir resultados no terminal
        predictions = results.pandas().xyxy[0]  # dataframe com as predições
        if not predictions.empty:
            for idx, row in predictions.iterrows():
                class_name = row['name']
                confidence = row['confidence']
                print(f"Detectado: {class_name} (Confiança: {confidence:.2f})")

        frame = np.squeeze(results.render())

        cv2.imshow('Deteccao', frame)

        key = cv2.waitKey(5)
        if key == ord('q'):
            break

    except Exception as e:
        print(f"Erro ao capturar ou processar a imagem: {e}")
        break

cv2.destroyAllWindows()

