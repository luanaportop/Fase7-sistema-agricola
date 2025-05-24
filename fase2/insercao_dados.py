import os
import pandas as pd
from conexao_mysql import conectar  

def inserir_dados_csv():
    # Caminho absoluto para o arquivo CSV
    caminho_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fase1dados.csv'))
    
    df = pd.read_csv(caminho_csv)
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    for _, row in df.iterrows():
        sql = '''
            INSERT INTO Cultura (nome_cultura, data_plantio, area_plantio)
            VALUES (%s, NOW(), %s)
        '''
        valores = (row['cultura'], row['area'])
        cursor.execute(sql, valores)
    
    conexao.commit()
    cursor.close()
    conexao.close()

if __name__ == '__main__':
    inserir_dados_csv()
