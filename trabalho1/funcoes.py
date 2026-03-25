import numpy as np

def vizinho_reducao(img):
    largura, altura = img.shape
    matriz_reduzida = np.zeros((largura // 2, altura // 2), dtype='uint8')

    for i in range(0, largura // 2):
        for j in range(0, altura // 2):
            matriz_reduzida[i][j] = img[i * 2][j * 2]
            
    return matriz_reduzida

def vizinho_ampliacao(img):
    largura, altura = img.shape
    matriz_ampliada = np.zeros((largura * 2, altura * 2), dtype='uint8')

    for i in range(0, largura):
        for j in range(0, altura):
            valor = img[i][j]
            matriz_ampliada[i*2][j*2] = valor
            matriz_ampliada[i*2+1][j*2] = valor
            matriz_ampliada[i*2][j*2+1] = valor
            matriz_ampliada[i*2+1][j*2+1] = valor
            
    return matriz_ampliada

def bilinear_reducao(img):
    largura, altura = img.shape
    matriz_reduzida = np.zeros((largura // 2, altura // 2), dtype='uint8')

    for i in range(0, largura // 2):
        for j in range(0, altura // 2):
            pixel = (int(img[i*2][j*2]) + int(img[i*2+1][j*2]) + 
                     int(img[i*2][j*2+1]) + int(img[i*2+1][j*2+1])) / 4
            matriz_reduzida[i][j] = int(pixel)
            
    return matriz_reduzida

def bilinear_ampliacao(img):
    largura, altura = img.shape
    matriz_ampliada = np.zeros((largura * 2, altura * 2), dtype='uint8')

    for i in range(0, largura):
        for j in range(0, altura):
            matriz_ampliada[i*2][j*2] = img[i][j]

            proximo_i = i + 1 if i < largura - 1 else i
            proximo_j = j + 1 if j < altura - 1 else j

            matriz_ampliada[i*2+1][j*2] = (int(img[i][j]) + int(img[proximo_i][j])) // 2
            matriz_ampliada[i*2][j*2+1] = (int(img[i][j]) + int(img[i][proximo_j])) // 2
            matriz_ampliada[i*2+1][j*2+1] = (int(img[i][j]) + int(img[proximo_i][j]) + int(img[i][proximo_j]) + int(img[proximo_i][proximo_j])) // 4
            
    return matriz_ampliada