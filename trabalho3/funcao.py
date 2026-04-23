from PIL import Image
import numpy as np

def aplicar_transformacao_negativa(caminho_entrada):

        imagem = Image.open(caminho_entrada).convert('L')
  
        dados_pixel = np.array(imagem)
        
        # Aplica a função de transformação: s = (L - 1) - r, onde L = 256 para imagens de 8 bits (cinza)
        resultado_negativo = 255 - dados_pixel
        
        imagem_final = Image.fromarray(resultado_negativo.astype('uint8'))
        
        return imagem_final