# fase4_dashboard/dashboard.py

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

@st.cache_data
def train_model(data):
    X = data.drop("irrigacao", axis=1)
    y = data["irrigacao"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return modelo, accuracy

def mostrar_dashboard():
    file_path = "dados_fase4.csv"
    data = load_data(file_path)
    modelo, accuracy = train_model(data)

    st.title("Dashboard de Irrigação Inteligente")
    st.write("Monitoramento em tempo real dos dados do sistema de irrigação")

    st.sidebar.header("Navegação")
    pagina = st.sidebar.radio("Escolha a página:", ["Monitoramento", "Teste de Novos Dados"])

    if pagina == "Monitoramento":
        st.subheader("Acurácia do Modelo de Machine Learning")
        st.write(f"Acurácia do modelo: **{accuracy:.2f}**")

        irrigacao_counts = data["irrigacao"].value_counts()
        st.subheader("Distribuição de Necessidade de Irrigação")
        st.bar_chart(irrigacao_counts, use_container_width=True)
        st.write(f"**Linhas que precisam de irrigação:** {irrigacao_counts.get(1, 0)}")
        st.write(f"**Linhas que não precisam de irrigação:** {irrigacao_counts.get(0, 0)}")

        st.subheader("Gráficos de Monitoramento")
        col1, col2 = st.columns(2)
        with col1:
            st.line_chart(data["umidade_solo"], use_container_width=True)
        with col2:
            st.line_chart(data["temperatura"], use_container_width=True)

        st.subheader("Dados do Sistema")
        st.dataframe(data)

        st.sidebar.header("Filtros")
        min_umidade = st.sidebar.slider("Umidade Mínima", min_value=0, max_value=100, value=30)
        data_filtrada = data[data["umidade_solo"] >= min_umidade]
        st.write("Dados Filtrados:")
        st.dataframe(data_filtrada)

    elif pagina == "Teste de Novos Dados":
        st.subheader("Teste de Novos Dados")
        umidade = st.number_input("Umidade do Solo", min_value=0.0, max_value=100.0, value=30.0)
        temperatura = st.number_input("Temperatura", min_value=-10.0, max_value=50.0, value=22.0)
        luminosidade = st.number_input("Luminosidade", min_value=0.0, max_value=1000.0, value=500.0)
        nutrientes_P = st.number_input("Nutrientes P", min_value=0.0, max_value=1.0, value=1.0)
        nutrientes_K = st.number_input("Nutrientes K", min_value=0.0, max_value=1.0, value=0.0)

        if st.button("Testar"):
            novo_dado = pd.DataFrame({
                "umidade_solo": [umidade],
                "temperatura": [temperatura],
                "luminosidade": [luminosidade],
                "nutrientes_P": [nutrientes_P],
                "nutrientes_K": [nutrientes_K]
            })
            predicao = modelo.predict(novo_dado)[0]
            st.write(f"Previsão de Irrigação: **{'Irrigar' if predicao == 1 else 'Não Irrigar'}**")
