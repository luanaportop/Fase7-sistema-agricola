# fase7_integracao/main.py

import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
# Importar as funções das outras fases
from fase4.src.front import mostrar_dashboard as dashboard_fase4
# Importe outras fases aqui, por exemplo:
from fase1.index import rodar_fase1
from fase2.index import rodar_fase2
from fase3.db_fase3 import BancoDeDados
from fase3.funcoes import (
    inserir_leitura,
    registrar_irrigacao,
    registrar_historico,
    atualizar_leitura,
    deletar_historico,
    obter_historico
)


import os
os.environ["STREAMLIT_WATCH_MODE"] = "false"

import torch


@st.cache_resource(show_spinner=True)
def carregar_modelo(path_modelo):
    model = torch.hub.load('fase6/yolov5', 'custom', path=path_modelo, source='local')
    return model

def rodar_fase6():
    st.title("Fase 6 - Visão Computacional com YOLOv5")

    uploaded_file = st.file_uploader("Envie uma imagem para detecção", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Imagem Original", use_column_width=True)

        model_path = "fase6/rede_neural_cap1_fase6-main/ir_alem/best.pt"
        model = carregar_modelo(model_path)

        results = model(np.array(image))

        st.write("Detecções:")

        df = results.pandas().xyxy[0]
        st.dataframe(df)

        img_result = results.render()[0]
        st.image(img_result, caption="Imagem com Detecção", use_column_width=True)


# No seu fluxo principal, chame rodar_fase6() na opção correta do menu


st.title("Sistema Integrado de Gestão Agro")

menu = st.sidebar.selectbox("Escolha a Fase para visualizar", [
    "Fase 1 - Cálculos de Área e Insumos",
    "Fase 2 - Banco de Dados",
    "Fase 3 - IoT e Automação",
    "Fase 4 - Dashboard de Irrigação",
    "Fase 6 - Visão Computacional"
])

if menu == "Fase 1 - Cálculos de Área e Insumos":
    rodar_fase1()

elif menu == "Fase 2 - Banco de Dados":
    rodar_fase2()


elif menu == "Fase 3 - IoT e Automação":
    st.header("Fase 3: IoT e Automação")

    tipo_sensor = st.text_input("Tipo do Sensor", value="Umidade")
    valor_sensor = st.number_input("Valor do Sensor", min_value=0.0, step=1.0)

    if st.button("Inserir Leitura"):
        inserir_leitura(tipo_sensor, valor_sensor)
        st.success(f"Leitura inserida: {tipo_sensor} = {valor_sensor}")

    if st.button("Registrar Irrigação (Ligado)"):
        registrar_irrigacao("Ligado")
        st.success("Irrigação registrada como 'Ligado'")

    if st.button("Registrar Histórico (ID fixo: sensor=1, irrigação=1)"):
        registrar_historico(1, 1)
        st.success("Histórico registrado")

    id_sensor_update = st.number_input("ID do Sensor para Atualizar", step=1)
    novo_valor = st.number_input("Novo Valor", min_value=0.0, step=1.0)
    if st.button("Atualizar Leitura"):
        atualizar_leitura(id_sensor_update, novo_valor)
        st.success("Leitura atualizada")

    id_historico_del = st.number_input("ID do Histórico para Deletar", step=1)
    if st.button("Deletar Histórico"):
        deletar_historico(id_historico_del)
        st.success("Histórico deletado")

    if st.button("Mostrar Histórico"):
        historico = obter_historico()
        st.write("Histórico de Irrigação:")
        st.table(historico)


elif menu == "Fase 4 - Dashboard de Irrigação":
    dashboard_fase4()

elif menu == "Fase 6 - Visão Computacional":
    rodar_fase6()
