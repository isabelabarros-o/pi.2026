#Alunos: Isabela Barros de Oliveira e Mateus Leopoldo

from funcoes import rotular_componentes

def exibir_matriz(titulo, matriz):
    print(f"\n{titulo}")
    for linha in matriz:
        print("  ".join(f"{val}" for val in linha))

if __name__ == "__main__":

    imagem_teste = [
        [1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 1]
    ]

    exibir_matriz("IMAGEM BINÁRIA ORIGINAL", imagem_teste)

    resultado = rotular_componentes(imagem_teste)

    exibir_matriz("RESULTADO DA ROTULAÇÃO (4-CONECTADA)", resultado)
