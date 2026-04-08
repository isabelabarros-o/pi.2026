def rotular_componentes(imagem_binaria):
    """
    4-conectividade

    """
    linhas = len(imagem_binaria)
    colunas = len(imagem_binaria[0])
    
    rotulos = [[0 for _ in range(colunas)] for _ in range(linhas)]
    proximo_rotulo = 1
    equivalencias = {}

    for i in range(linhas):
        for j in range(colunas):
            if imagem_binaria[i][j] == 1:
                a = rotulos[i-1][j] if i > 0 else 0
                e = rotulos[i][j-1] if j > 0 else 0
                #a = acima, e = esquerda

                if a == 0 and e == 0:
                    rotulos[i][j] = proximo_rotulo
                    equivalencias[proximo_rotulo] = proximo_rotulo
                    proximo_rotulo += 1
                
                elif (a != 0 and e == 0) or (a == 0 and e != 0):
                    rotulos[i][j] = a if a != 0 else e
                
                elif a != 0 and e != 0:
                    if a == e:
                        rotulos[i][j] = a
                    else:
                        menor = min(a, e)
                        maior = max(a, e)
                        rotulos[i][j] = menor
                        equivalencias[maior] = buscar_raiz(equivalencias, menor)

    for i in range(linhas):
        for j in range(colunas):
            if rotulos[i][j] > 0:
                rotulos[i][j] = buscar_raiz(equivalencias, rotulos[i][j])

    return rotulos

def buscar_raiz(equivalencias, label):
    """função auxiliar para encontrar a classe de equivalência final"""
    while equivalencias[label] != label:
        label = equivalencias[label]
    return label