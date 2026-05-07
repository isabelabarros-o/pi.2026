# Processamento de Imagens (2026/1)

Este repositório contém as implementações práticas desenvolvidas durante a disciplina de Processamento de Imagens no curso de **Ciência da Computação** da **Universidade Federal do Tocantins (UFT)**.

**Aluna:** Isabela Barros de Oliveira  
**Professora:** Dra. Glenda Botelho  
**Instituição:** Universidade Federal do Tocantins - Campus Palmas  


---

## 🛠️ Tecnologias e Bibliotecas
Para garantir eficiência no processamento de matrizes e manipulação de arquivos de imagem, foram utilizadas:
* **Python**: Linguagem base para todos os algoritmos.
* **NumPy**: Manipulação de matrizes e cálculos matemáticos.
* **Pillow (PIL)**: Carregamento, tratamento de metadados e exibição de imagens.


---

## 🚀 Trabalhos Desenvolvidos

### 🚀 Trabalho 1: Reamostragem e Interpolação
Implementação de algoritmos para alteração da resolução espacial de imagens, explorando diferentes métodos de preenchimento de pixels:
* **Vizinho Mais Próximo**: Atribui ao novo pixel o valor da intensidade do pixel mais próximo na imagem original.
* **Interpolação Bilinear**: Utiliza os quatro vizinhos mais próximos para calcular a nova intensidade através de uma média ponderada, garantindo resultados mais suaves.

### 🚀 Trabalho 2: Rotulação de Componentes Conectados
Implementação do algorítmo de rotulação, considerando os conceitos vistos na aula (imagens binárias).

### 🚀 Trabalho 3: Transformação de Intensidade Negativa
Implementação de processamento pontual no domínio espacial para inversão de tons.
* **Teoria**: Aplicação da função de transformação $s = (L - 1) - r$.
* **Objetivo**: Inverter os níveis de cinza da imagem para realçar detalhes claros em áreas predominantemente escuras.


---

## 📖 Referências
* GONZALEZ, Rafael C.; WOODS, Richard E. **Processamento Digital de Imagens**. 3ª Edição.
* Material didático da disciplina (apresentações de slide).


---
