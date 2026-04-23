
from funcao import aplicar_transformacao_negativa


def main():
    img_original = "trabalho3/luna.jpeg"
    
    img_negativa = aplicar_transformacao_negativa(img_original)
    
    if img_negativa:
        img_negativa.save("trabalho3/resultado_negativo.jpg")
      
        img_negativa.show()
        print("Transformação concluída com sucesso!")

if __name__ == "__main__":
    main()