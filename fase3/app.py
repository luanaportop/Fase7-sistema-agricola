import streamlit as st
from db import inserir_sensor, listar_dados

st.set_page_config(page_title="Gestão de Sensores - AgroTech", layout="wide")

# Sidebar
st.sidebar.title("Menu")
menu = st.sidebar.radio("Escolha uma opção", ["Registrar", "Consultar", "Atualizar", "Deletar", "Controle Irrigação"])

# REGISTRAR DADOS
if menu == "Registrar":
    st.header("📥 Registrar Leitura dos Sensores")
    ph = st.number_input("pH do Solo", step=0.1)
    fosforo = st.selectbox("Fósforo presente?", ['S', 'N'])
    potassio = st.selectbox("Potássio presente?", ['S', 'N'])
    umidade = st.number_input("Umidade (%)", step=0.1)
    temperatura = st.number_input("Temperatura (°C)", step=0.1)

    if st.button("Salvar dados"):
        inserir_sensor(ph, fosforo, potassio, umidade, temperatura)
        st.success("Dados salvos com sucesso!")

# CONSULTAR DADOS
elif menu == "Consultar":
    st.header("🔎 Leitura dos Sensores Registrados")
    df = listar_dados()
    if df.empty:
        st.info("Nenhum dado registrado ainda.")
    else:
        st.dataframe(df)
