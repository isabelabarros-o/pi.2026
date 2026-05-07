"""
Alunos: Isabela Barros e Mateus Leopoldo
"""

import cv2
import numpy as np


def aplicar_abertura(caminho_imagem, kernel_size=5):
    """
    Abertura: erosão seguida de dilatação.
    
    Efeito: remove ruído pequeno (pontos brancos espalhados) mantendo objetos grandes.
    
    Args:
        caminho_imagem (str): Caminho da imagem a processar
        kernel_size (int): Tamanho do kernel
    
    Returns:
        imagem_aberta (numpy.ndarray): Imagem após abertura
    """
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    imagem_aberta = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, kernel)
    return imagem_aberta


def aplicar_fechamento(caminho_imagem, kernel_size=5):
    """
    Fechamento: dilatação seguida de erosão.
    
    Efeito: preenche buracos pequenos nos objetos brancos.
    
    Args:
        caminho_imagem (str): Caminho da imagem a processar
        kernel_size (int): Tamanho do kernel
    
    Returns:
        imagem_fechada (numpy.ndarray): Imagem após fechamento
    """
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    imagem_fechada = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, kernel)
    return imagem_fechada



if __name__ == "__main__":
    
    imagem_aberta = aplicar_abertura("trabalho5/minha_imagem.jpg")
    cv2.imwrite("trabalho5/resultado_abertura.jpg", imagem_aberta)

    imagem_fechada = aplicar_fechamento("trabalho5/minha_imagem.jpg")
    cv2.imwrite("trabalho5/resultado_fechamento.jpg", imagem_fechada)

    print("Abertura e Fechamento feitos com sucesso!")



