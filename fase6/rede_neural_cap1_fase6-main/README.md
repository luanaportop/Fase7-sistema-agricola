# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Despertar da rede neural

## Beginner Coders

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/luana-porto-pereira-gomes/">Luana Porto Pereira Gomes</a>
- <a href="https://www.linkedin.com/in/luma-x">Luma Oliveira</a>
- <a href="https://www.linkedin.com/in/priscilla-oliveira-023007333/">Priscilla Oliveira </a>
- <a href="https://www.linkedin.com/in/paulobernardesqs?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app">Paulo Bernardes</a>  

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>


## 📜 Descrição

implementação da Entrega 1 e Entrega 2 da Fase 6 do projeto interdisciplinar (PBL) do curso de Inteligência Artificial da FIAP. 
Nesta fase, desenvolvemos um sistema de visão computacional utilizando o modelo YOLOv5 e uma CNN do zero para detecção e classificação de objetos com foco em aplicações práticas para a empresa fictícia FarmTech Solutions, 
que atua no agronegócio, saúde animal, segurança patrimonial, entre outras áreas.

## 📝 Sobre o Projeto
Foram utilizados dois tipos de dados:
- **NDVI (índice de vegetação)** obtido do sistema SATVeg da Embrapa.
- **Produtividade agrícola (rendimento médio)** obtido do sistema IBGE/SIDRA.
O trabalho foi desenvolvido como parte da Sprint 2 do Enterprise Challenge da 
FIAP, no 2º semestre do curso de Inteligência Artificial.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>dados</b>: aqui estão os dados utilizados no notebook.
  
- <b>notebook</b>: aqui está o download do notebook em .ipynb.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código
### ✅ YOLOv5 no Google Colab

    Acesse o notebook com todas as etapas documentadas:
    👉 https://colab.research.google.com/drive/1YXuF5M4vYb3JInyeuZtwW0_T4cHB0uq8?usp=sharing

    Verifique se os arquivos do dataset e as anotações estão organizados no seu Google Drive.

    Execute todas as células do notebook em sequência, observando:

        Treinamento com duas variações de épocas (30 e 60)

        Validação e testes com imagens novas

        Análise comparativa dos resultados obtidos


## 🎥 Link do vídeo: (https://youtu.be/Ml2_Ubd3A3A)

🧠 CNN treinada do zero

A implementação da CNN do zero também está disponível no notebook acima, em seção separada, com análises críticas de desempenho.
🧪 Etapas Realizadas
🔹 Entrega 1 – YOLO Customizado

    Coleta e organização de 80 imagens de dois objetos distintos.

    Separação dos dados em treino, validação e teste (32/4/4 por classe).

    Anotação via Make Sense AI.

    Treinamento do modelo YOLOv5 com 30 e 60 épocas.

    Avaliação comparativa de resultados.

    Prints de imagens processadas para demonstração ao cliente da FarmTech.

🔹 Entrega 2 – Comparação de Modelos

    Implementação da YOLO tradicional.

    Treinamento de uma CNN do zero.

    Análise crítica:

        Facilidade de uso

        Precisão

        Tempo de treino e inferência

        Integração e desempenho

⭐ “Ir Além” – Reconhecimento em tempo real com ESP32-CAM

    Utilização do ESP32-CAM com comunicação Wi-Fi.

    Integração com o Python utilizando o modelo best.pt.

    Processamento de imagens capturadas com reconhecimento local.

    Documentação do sistema com arquitetura, imagens, código e justificativa.

    Demonstração prática em vídeo.

🎥 Demonstrações em Vídeo

    🔗 Entrega 1 + 2: Assista no YouTube: https://youtu.be/Ml2_Ubd3A3A

    🔗 Ir Além - ESP32-CAM: Assista no YouTube: https://youtu.be/I5PSV_cWrBo


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
