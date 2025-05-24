import streamlit as st
import csv
import os
import pandas as pd
import boto3
import subprocess


ARQUIVO_CSV = "fase1dados.csv"
NOME_BUCKET_S3 = "fiap-fase7-pb" 
AWS_ACCESS_KEY_ID= 'AKIAVVZOODHI474HEBW6'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = "us-east-1"

def upload_arquivo_para_s3(caminho_arquivo_local, nome_arquivo_s3, nome_bucket):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    try:
        s3.upload_file(caminho_arquivo_local, nome_bucket, nome_arquivo_s3)
        st.info(f"Arquivo enviado para o S3: s3://{nome_bucket}/{nome_arquivo_s3}")
    except Exception as e:
        st.error(f"Erro ao enviar arquivo para o S3: {e}")



def carregar_dados():
    dados = []
    if os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['area'] = float(row['area'])
                row['insumo'] = float(row['insumo'])
                dados.append(row)
    return dados

def salvar_dados(dados):
    with open(ARQUIVO_CSV, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "cultura", "area", "insumo"])
        writer.writeheader()
        writer.writerows(dados)
        
    upload_arquivo_para_s3(ARQUIVO_CSV, ARQUIVO_CSV, NOME_BUCKET_S3)
    
    # Caminho absoluto do script R (considerando que index.py e statistic.r estão na mesma pasta)
    script_r = os.path.join(os.path.dirname(__file__), "statistic.r")
    
    # Executa o script R via Rscript (certifique-se que Rscript está no PATH)
    try:
        subprocess.run(["Rscript", script_r], check=True)
        print("Script R executado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script R: {e}")


def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_insumos(area, quantidade_por_metro):
    return area * quantidade_por_metro

def rodar_fase1():
    st.subheader("Cadastro de Dados Agrícolas")
    dados = carregar_dados()

    df_resultados = pd.read_csv('resultados_estatisticos.csv')

    st.title("Resultados Estatísticos do Agronegócio")
    st.table(df_resultados)


    menu = ["Inserir dados", "Atualizar dados", "Deletar dados", "Mostrar dados", "Sair"]
    escolha = st.selectbox("Escolha uma opção:", menu)

    if escolha == "Inserir dados":
        cultura = st.radio("Escolha a cultura:", ["Milho", "Soja"])

        if cultura == "Milho":
            comprimento = st.number_input("Comprimento do campo (m):", min_value=0.0)
            largura = st.number_input("Largura do campo (m):", min_value=0.0)
            quantidade_por_metro = st.number_input("Quantidade de insumo por metro²:", min_value=0.0)
            if st.button("Calcular e Salvar Milho"):
                area = calcular_area_retangulo(comprimento, largura)
                insumo = calcular_insumos(area, quantidade_por_metro)
                novo_id = max([d['id'] for d in dados], default=0) + 1
                dados.append({
                    "id": novo_id,
                    "cultura": "Milho",
                    "area": area,
                    "insumo": insumo
                })
                salvar_dados(dados)
                st.success(f"Área: {area} m² | Insumo: {insumo} litros")

        elif cultura == "Soja":
            base = st.number_input("Base do campo (m):", min_value=0.0)
            altura = st.number_input("Altura do campo (m):", min_value=0.0)
            quantidade_por_metro = st.number_input("Quantidade de insumo por metro²:", min_value=0.0)
            if st.button("Calcular e Salvar Soja"):
                area = calcular_area_triangulo(base, altura)
                insumo = calcular_insumos(area, quantidade_por_metro)
                novo_id = max([d['id'] for d in dados], default=0) + 1
                dados.append({
                    "id": novo_id,
                    "cultura": "Soja",
                    "area": area,
                    "insumo": insumo
                })
                salvar_dados(dados)
                st.success(f"Área: {area} m² | Insumo: {insumo} litros")

    elif escolha == "Atualizar dados":
        if not dados:
            st.warning("Nenhum dado disponível para atualizar.")
        else:
            ids = [d['id'] for d in dados]
            id_selecionado = st.selectbox("Selecione o ID para atualizar:", ids)
            registro = next((d for d in dados if d['id'] == id_selecionado), None)
            if registro:
                nova_cultura = st.radio("Cultura:", ["Milho", "Soja"], index=["Milho","Soja"].index(registro['cultura']))
                if nova_cultura == "Milho":
                    comprimento = st.number_input("Comprimento do campo (m):", value=registro['area']**0.5)
                    largura = st.number_input("Largura do campo (m):", value=registro['area']**0.5)
                    quantidade_por_metro = st.number_input("Quantidade de insumo por metro²:", value=registro['insumo']/registro['area'])
                    if st.button("Atualizar Milho"):
                        area = calcular_area_retangulo(comprimento, largura)
                        insumo = calcular_insumos(area, quantidade_por_metro)
                        registro.update({"cultura": "Milho", "area": area, "insumo": insumo})
                        salvar_dados(dados)
                        st.success("Registro atualizado!")
                else:
                    base = st.number_input("Base do campo (m):", value=registro['area']**0.5)
                    altura = st.number_input("Altura do campo (m):", value=registro['area']**0.5)
                    quantidade_por_metro = st.number_input("Quantidade de insumo por metro²:", value=registro['insumo']/registro['area'])
                    if st.button("Atualizar Soja"):
                        area = calcular_area_triangulo(base, altura)
                        insumo = calcular_insumos(area, quantidade_por_metro)
                        registro.update({"cultura": "Soja", "area": area, "insumo": insumo})
                        salvar_dados(dados)
                        st.success("Registro atualizado!")

    elif escolha == "Deletar dados":
        if not dados:
            st.warning("Nenhum dado disponível para deletar.")
        else:
            ids = [d['id'] for d in dados]
            id_selecionado = st.selectbox("Selecione o ID para deletar:", ids)
            if st.button("Deletar"):
                dados = [d for d in dados if d['id'] != id_selecionado]
                salvar_dados(dados)
                st.success("Registro deletado!")

    elif escolha == "Mostrar dados":
        if not dados:
            st.warning("Nenhum dado disponível.")
        else:
            for d in dados:
                st.write(f"ID: {d['id']}")
                st.write(f"Cultura: {d['cultura']}")
                st.write(f"Área: {d['area']} metros quadrados")
                st.write(f"Insumo necessário: {d['insumo']} litros")
                st.markdown("---")

    elif escolha == "Sair":
        st.write("Saindo da fase 1.")
