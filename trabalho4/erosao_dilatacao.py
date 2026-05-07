import cv2
import numpy as np

def funcao(caminho_imagem):
    img = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    if img is None: return
    _, binaria = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    h, w = binaria.shape
    k_size = 5
    offset = k_size // 2
    

    img_erosao = np.zeros((h, w), np.uint8)
    img_dilatacao = np.zeros((h, w), np.uint8)

    for i in range(offset, h - offset):
        for j in range(offset, w - offset):
            
            janela = binaria[i-offset : i+offset+1, j-offset : j+offset+1]

            img_dilatacao[i, j] = np.max(janela)
    
            img_erosao[i, j] = np.min(janela)

    return img_erosao, img_dilatacao


erosao, dilatacao = funcao("trabalho4/minha_imagem.jpg")
cv2.imwrite("trabalho4/resultado_erosao.jpg", erosao)
cv2.imwrite("trabalho4/resultado_dilatacao.jpg", dilatacao) 