import pandas as pd
import numpy as np

# Carregar o CSV existente
dados = pd.read_csv('dados_irrigacao.csv')

# Verificar a estrutura dos dados
print(dados.head())

# 1. Gerar dados sintéticos com base nas correlações
np.random.seed(42)

# Funções para gerar dados sintéticos (com base nas distribuições das colunas)
def gerar_umidade():
    return np.random.uniform(30, 80)  # Faixa de umidade do solo (ajustar conforme necessário)

def gerar_temperatura():
    return np.random.uniform(15, 35)  # Faixa de temperatura (ajustar conforme necessário)

def gerar_luminosidade():
    return np.random.uniform(300, 1000)  # Faixa de luminosidade (ajustar conforme necessário)

def gerar_nutrientes_P():
    return np.random.uniform(0, 1)  # Nutriente P (ajustar conforme necessário)

def gerar_nutrientes_K():
    return np.random.uniform(0, 1)  # Nutriente K (ajustar conforme necessário)

def gerar_irrigacao(umidade, temperatura, luminosidade, nutrientes_K):
    # Modelo simplificado de previsão de irrigação com base nas variáveis (ajustar conforme necessidade)
    if umidade < 40 or temperatura > 30 or luminosidade > 800 or nutrientes_K < 0.3:
        return 1  # Irrigar
    else:
        return 0  # Não irrigar

# Gerar mais 500 amostras de dados sintéticos
novos_dados = []
for _ in range(2000):  # Ajustar número de dados gerados
    umidade = gerar_umidade()
    temperatura = gerar_temperatura()
    luminosidade = gerar_luminosidade()
    nutrientes_P = gerar_nutrientes_P()
    nutrientes_K = gerar_nutrientes_K()
    irrigacao = gerar_irrigacao(umidade, temperatura, luminosidade, nutrientes_K)
    
    novos_dados.append([umidade, temperatura, luminosidade, nutrientes_P, nutrientes_K, irrigacao])

# Criar um novo DataFrame com os dados sintéticos
novos_dados_df = pd.DataFrame(novos_dados, columns=['umidade_solo', 'temperatura', 'luminosidade', 'nutrientes_P', 'nutrientes_K', 'irrigacao'])

# Concatenar com o DataFrame original para aumentar os dados
dados_completos = pd.concat([dados, novos_dados_df], ignore_index=True)

# Salvar o novo CSV com os dados aumentados
dados_completos.to_csv('dados_irrigacao_aumentados.csv', index=False)

print(f"Novo dataset com {len(dados_completos)} linhas salvo como 'dados_irrigacao_aumentados.csv'")
