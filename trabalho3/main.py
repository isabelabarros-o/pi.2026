
from funcao import aplicar_transformacao_negativa


def main():
    img_original = "trabalho3/img2.png"
    
    img_negativa = aplicar_transformacao_negativa(img_original)
    
    if img_negativa:
        img_negativa.save("trabalho3/resultado_negativo2s.png")
      
        img_negativa.show()
        print("Transformação concluída com sucesso!")

if __name__ == "__main__":
    main()