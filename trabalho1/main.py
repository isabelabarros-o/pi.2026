from PIL import Image
import numpy as np
from funcoes import vizinho_reducao, vizinho_ampliacao, bilinear_reducao, bilinear_ampliacao


imagem = Image.open("trabalho1\cachorro_bobo.jpeg").convert('L')
img_matriz = np.array(imagem)

vizinho_reducao = vizinho_reducao(img_matriz)
Image.fromarray(vizinho_reducao).save('imagem_vizinho_reducao.jpg')

vizinho_ampliacao = vizinho_ampliacao(img_matriz)
Image.fromarray(vizinho_ampliacao).save('imagem_vizinho_ampliacao.jpg')


bilinear_ampliacao = bilinear_ampliacao(img_matriz)
Image.fromarray(bilinear_ampliacao).save('imagem_bilinear_ampliacao.jpg')

bilinear_reducao = bilinear_reducao(img_matriz)
Image.fromarray(bilinear_reducao).save('imagem_bilinear_reducao.jpg')

print("Processamento concluído!")
