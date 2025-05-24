# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions - Fase 4

## Beginner Coders

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/luana-porto-pereira-gomes/">Luana Porto Pereira Gomes</a>
- <a href="https://www.linkedin.com/in/priscilla-oliveira-023007333/">Priscilla Oliveira </a>
- <a href="https://www.linkedin.com/in/paulobernardesqs?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app">Paulo Bernardes</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>


## 📜 Descrição

Este repositório apresenta as melhorias realizadas no projeto da Fase 3 da FarmTech Solutions. A seguir, os principais objetivos desta fase:

## Objetivos
- [x] Incorporar Scikit-learn para previsão de irrigação.
- [x] Criar um dashboard interativo com Streamlit.
- [x] Adicionar um display LCD para exibir métricas no ESP32 (simulado no Wokwi).
- [x] Monitorar variáveis no Serial Plotter.
- [x] Otimizar o uso de memória no código C/C++ do ESP32. 
- [x] Melhoria no Banco de Dados.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão as imagens do banco de dados relacional e do funcionamento do Serial Plotter.

- <b>scripts</b>: aqui está um código python auxiliar para gerar dados ----------

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto. Código principal (main.py), código de modelagem preditiva Scikit-learn (modelagem.py), código de interface interativa (front.py), código C++ do circuito ESP32 (cod.cpp) e arquivo csv usado para o código de modelagem preditiva e interface interativa.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*
#### Código Python:
   - Tenha uma IDE que possibilite a execução do código.
   - Instale as bibliotecas necessárias para os códigos:
        main.py: oracledb, pandas e os.
        modelagem.py: pandas, numpy, scikit-learn.
        front.py: streamlit, pandas, matplotlib, numpy, scikit-learn.
   - Baixe o arquivo csv disponibilizado.
   - Crie as tabelas do banco de dados oracle e faça a conexão com seu usuário e senha.
#### Código C++:
   - Abra o link do circuito wokwi: https://wokwi.com/projects/415903032457764865
   - Instale as bibliotecas: DHT.h, Wire.h, LiquidCrystal_I2C.h


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - 03/12/2024
    *

## Melhorias do projeto FarmTech Solutions
### Circuito ESP32:
#### **Funcionalidades do Sistema**
1. **Leitura de Sensores:**
   - **DHT22:** Temperatura e umidade relativa.
   - **LDR:** Simula a umidade do solo.
   - **Potenciômetros:** Simulam os níveis de potássio e fósforo no solo.

2. **Controle Automático da Bomba:**
   - A bomba é ativada automaticamente se a umidade do solo estiver abaixo de 30%.
   - O estado da bomba é exibido no display LCD e no Serial Plotter.

3. **Exibição no Display LCD (20x4, I2C):**
   - Linha 1: Temperatura e umidade relativa.
   - Linha 2: Umidade do solo.
   - Linha 3: Níveis de potássio e fósforo.
   - Linha 4: Estado da bomba (Ligada/Desligada).

4. **Serial Plotter:**
   - Exibe gráficos em tempo real das variáveis:
     - Temperatura.
     - Umidade relativa.
     - Umidade do solo.
     - Potássio e fósforo.
     - Estado da bomba.
       
   <a href= "#"><img src="assets/SP-1.png" alt="Serial Plotter" border="0" width=40% height=40%></a>
   <a href= "#"><img src="assets/SP-2.png" alt="Serial Plotter" border="0" width=40% height=40%></a>
   <a href= "#"><img src="assets/SP-3.png" alt="Serial Plotter" border="0" width=40% height=40%></a>

---

#### **Melhorias Implementadas**
- Normalizamos a leitura do LDR para uma escala de 0 a 100%.
- Utilizamos potenciômetros como simuladores para os níveis de potássio e fósforo.
- Normalizamos a leitura do potenciômetro para: Potássio (Escala de 0 a 100 mg/dm³) e fósforo (Escala de 0 a 30 mg/dm³).
- Estabelecemos os limites médios ideais de potássio (60 mg/dm³) e fósforo (15 mg/dm³) no solo.
- Normalizamos a leitura do DHT22 para exibir os valores com duas casas decimais (temperatura e umidade relativa).
- Otimização do código: Reduzimos redundâncias e organizamos as funções para maior clareza e a justamos o intervalo de leituras para 5 segundos.
- Adicionamos mensagens de aviso para níveis críticos de potássio, fósforo e umidade do solo.

### Código Python e Banco de dados:
#### **Melhorias Implementadas**
Banco de dados:
- Substituimos a tabela t_sensor para t_leitura para deixar o banco de dados mais coerente com o projeto.
- Ajuste do tipo de dado do campo de leitura do potássio e do fósforo de char para float.
- Adicionamos à tabela t_leitura o campo de status_irrigacao.
- Substituimos na tabela t_irrigacao o campo data_hora para irrigacao_cultura, permitindo que o usuário tenha controle da irrigaçao de cada cultura utilizada.

<a href= "#"><img src="assets/modelo-relacional.png" alt="Serial Plotter" border="0" width=40% height=40%></a>

Código Python:
- Adicionamos o armazenamento da cultura do solo.
- Adicionamos a condição para o status da bomba (ativada/desativada).
- O controle da irrigação agora é feito a partir da escolha da data em que o usuário deseja saber qual foi o status da bomba (ativada/desativada).

## Links
- Link do vídeo: https://youtu.be/7uJsPhI4X_k?si=sa0lBb4SR6A7abQj
- Link do circuito wokwi: https://wokwi.com/projects/415903032457764865

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
