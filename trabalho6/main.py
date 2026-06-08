import cv2
import numpy as np
from filtro import filtro_media_manual

def main():
    caminho_imagem = 'trabalho6/borboleta.jpg'
    tamanho_kernel = 5 

    imagem_original = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    
    resultado = filtro_media_manual(caminho_imagem, tamanho_kernel)
    
    if resultado is not None and imagem_original is not None:
        try:
            cv2.imwrite('trabalho6/borboleta_filtrada.jpg', resultado)
        except Exception:
            pass
        cv2.imshow('Imagem Filtrada', resultado)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    else:
        print("Falha ao aplicar o filtro. Verifique se o arquivo 'borboleta.jpg' está na mesma pasta.")

if __name__ == "__main__":
    main()