import cv2
import numpy as np

def filtro_media_manual(caminho_imagem, tamanho_kernel=3):
    """
    Aplica o Filtro da Média em uma imagem em tons de cinza.
    Trata as bordas utilizando a técnica de Zero Padding.
    
    Args:
        caminho_imagem (str): Caminho para a imagem de entrada.
        tamanho_kernel (int): Tamanho da máscara quadrada (ex: 3 para 3x3).
        
    Returns:
        numpy.ndarray: Imagem filtrada (suavizada).
    """
    img = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Erro ao carregar a imagem.")
        return None
        
    h, w = img.shape
    offset = tamanho_kernel // 2
    
    img_padded = np.zeros((h + 2 * offset, w + 2 * offset), dtype=np.uint8)
    img_padded[offset : offset + h, offset : offset + w] = img
    
    img_filtrada = np.zeros((h, w), dtype=np.uint8)
    
    total_pixels_kernel = tamanho_kernel * tamanho_kernel

    for i in range(h):
        for j in range(w):
            vizinhanca = img_padded[i : i + tamanho_kernel, j : j + tamanho_kernel]
            
            soma_local = np.sum(vizinhanca)
            media = soma_local / total_pixels_kernel
            
            img_filtrada[i, j] = int(media)
            
    return img_filtrada
