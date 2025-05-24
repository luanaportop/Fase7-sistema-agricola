import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from fase2.db_config import DATABASE_URL  
from .etl_csv_db import importar_dados_fase1


def rodar_fase2():
    st.title("Fase 2 – Banco de Dados Estruturado")

    engine = create_engine(DATABASE_URL)
    with engine.begin() as conn:
        conn.execute(text("SELECT 1"))

    if st.button("📥 Importar CSV da Fase 1"):
        importar_dados_fase1()
        st.success("Dados importados!")

    if st.button("🔍 Visualizar Cultura"):
        df = pd.read_sql("SELECT * FROM Cultura", engine)
        st.dataframe(df)
