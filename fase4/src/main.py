# instalando bibliotecas

import oracledb
import pandas as pd
import os

#conectando banco de dados
try:
    conn = oracledb.connect(user='rm559290', password='161000', dsn='oracle.fiap.com.br:1521/ORCL') # Inserir user e password correspondente
    #CRUD
    var_create = conn.cursor()
    var_read = conn.cursor()
    var_update = conn.cursor()
    var_delete = conn.cursor()

except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    conexao = True
if conexao:
    print("Conexão estabelecida com sucesso.")
    print()
else:
    print("Falha na conexão.")

# Funções

def create_dados():
    while True:
        try:
            print("-------Registrar-------")
            cultura = input("Digite a cultura da irrigação: ")
            ph = float(input("Digite a leitura do sensor de PH: "))
            fosforo = float(input("Quantidade de fósforo no solo (mg/dm3): "))
            potassio = float(input("Quantidade de potássio no solo (mg/dm3): "))
            umidade = float(input("Digite a leitura do sensor de Umidade (%): "))
            temperatura = float(input("Digite a leitura do sensor de Temperatura (°C): "))
            status = "Desativada"
            if umidade < 30:
                status = "Ativada"

            sql = """
                INSERT INTO t_leitura (id_leitura, leitura_ph, leitura_fosforo_p, leitura_potassio_k, leitura_umidade, leitura_temperatura, status_irrigacao)
                VALUES (leitura_seq.NEXTVAL, :ph, :fosforo, :potassio, :umidade, :temperatura, :status)
                RETURNING id_leitura INTO :id
            """
            id_var = var_create.var(oracledb.NUMBER)  
            var_create.execute(sql, {
                'ph': ph,
                'fosforo': fosforo,
                'potassio': potassio,
                'umidade': umidade,
                'temperatura': temperatura,
                'status': status,
                'id': id_var
            })
            conn.commit()

            last_inserted_id = id_var.getvalue()[0]
            if last_inserted_id:
                sql_irrigacao = """
                    INSERT INTO t_irrigacao (id_irrigacao, id_leitura, irrigacao_cultura)
                    VALUES (irrigacao_seq.NEXTVAL, :id_leitura, :cultura)
                """
                var_create.execute(sql_irrigacao, {
                    'id_leitura': last_inserted_id,
                    'cultura': cultura
                })
                conn.commit()
            else:
                print("ID não foi retornado.")

        except ValueError:
            print("Digite um número válido!")
        except Exception as e:
            print("Algo deu errado: ", e)
        else:
            print("DADOS ARMAZENADOS")

        continuar = input("Deseja inserir outros dados? (s/n): ").strip().lower()
        if continuar != 's':
            break

def consulta_dados():
    print("-------- CONSULTAR --------")

    lista_dados = []
    try:
        consulta = "SELECT * FROM t_leitura"
        var_read.execute(consulta)

        data = var_read.fetchall()
        for dt in data:
            lista_dados.append(dt)

        lista_dados.sort()

        data_frame_dados = pd.DataFrame.from_records(lista_dados, columns=['id_leitura', 'leitura_ph', 'leitura_fosforo_p', 'leitura_potassio_k', 'leitura_umidade', 'leitura_temperatura', 'data_hora', 'status_irrigacao'])
        data_frame_dados['data_hora'] = pd.to_datetime(data_frame_dados['data_hora']).dt.strftime('%Y-%m-%d %H:%M:%S')

        if data_frame_dados.empty:
            print("Não há dados armazenados!")
        else:
            print(data_frame_dados.to_string(index=False))

    except Exception as e:
        print("Algo deu errado:", e)

def update_dados():
    try:
        print("-------Atualizar-------")
        leitura_id = int(input("Escolha um ID: "))

        # Verificar se o sensor existe
        consulta = "SELECT * FROM t_leitura WHERE id_leitura = :1"
        var_read.execute(consulta, (leitura_id,))
        data = var_read.fetchall()

        if len(data) == 0:
            print(f"Não existe sensor com o ID = {leitura_id}")
        else:
            # Pedir novos valores ao usuário
            novo_ph = float(input("Digite um novo valor para leitura do sensor de PH: "))
            novo_fosforo = float(input("Quantidade de fósforo no solo (mg/dm3): "))
            novo_potassio = float(input("Quantidade de potássio no solo (mg/dm3): "))
            nova_umidade = float(input("Digite um novo valor para leitura do sensor de Umidade: "))
            nova_temperatura = float(input("Digite um novo valor para leitura do sensor de Temperatura (°C): "))

            novo_status = "Desativada"
            if nova_umidade < 30:
                novo_status = "Ativada"

            # Atualizar os dados
            atualizar = """
                UPDATE t_leitura
                SET leitura_ph = :1, leitura_fosforo_p = :2, leitura_potassio_k = :3, leitura_umidade = :4, leitura_temperatura = :5, status_irrigacao = :6
                WHERE id_leitura = :7
            """
            var_update.execute(atualizar, (novo_ph, novo_fosforo, novo_potassio, nova_umidade, nova_temperatura, novo_status, leitura_id))
            conn.commit()
            print("Dados atualizados com sucesso!")
    except ValueError as e:
        print("Erro de valor, por favor insira um número válido.", e)
    except Exception as e:
        print("Algo deu errado!", e)

def consulta_irrigacao_por_data():
    try:
        print("-------- CONSULTAR IRRIGAÇÃO POR DATA --------")
        dia = int(input("Digite o dia (DD): "))
        mes = int(input("Digite o mês (MM): "))
        ano = int(input("Digite o ano (YYYY): "))

        # Formata a data para o padrão correto
        data_formatada = f"{dia:02d}/{mes:02d}/{ano}"

        sql = """
        SELECT TRIM(i.irrigacao_cultura), l.status_irrigacao AS status_irrigacao
        FROM t_irrigacao i
        JOIN t_leitura l ON i.id_leitura = l.id_leitura
        WHERE TRUNC(l.data_hora) = TO_DATE(:data, 'DD/MM/YYYY')
        """
        
        var_read.execute(sql, {'data': data_formatada})
        resultados = var_read.fetchall()

        # Verificação e exibição dos resultados
        if resultados:
            df = pd.DataFrame(resultados, columns=['Cultura', 'Status Irrigacao'])
            print(df.to_string(index=False))
        else:
            print("Nenhuma irrigação encontrada para a data fornecida.")
            
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
    except oracledb.DatabaseError as e:
        error, = e.args
        print("Erro de banco de dados:", error.message)
    except Exception as e:
        print("Erro ao consultar irrigações:", e)

def delet_dados():
    print("-------- DELETAR --------")

    escolha_id = input("Escolha um ID: ")

    if escolha_id.isdigit():
        escolha_id = int(escolha_id)

        try:
            consulta = "SELECT * FROM t_sensor WHERE id_sensor = :id"
            var_read.execute(consulta, [escolha_id])
            dado = var_read.fetchone()

            if dado:
                deletar = f"""DELETE FROM t_sensor WHERE id_sensor = {escolha_id}"""
                var_delete.execute(deletar)
                conn.commit()
                print("Dados deletados com sucesso!")
            else:
                print(f"Não há dados com o ID = {escolha_id}")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    else:
        print("O ID fornecido não é válido.")

# MENU
while conexao:

    # Menu
    print("-------------MENU-------------")
    print(""""
    1 - Registrar dados
    2 - Listar dados
    3 - Atualizar dados
    4 - Deletar dados
    5 - Controle irrigação
    6 - Sair
    """)
    # input
    escolha = input("Escolha um número: ")

    if escolha.isdigit():
        escolha = int(escolha)
    else:
        print("Digite um número!")
        continue

    

    if escolha == 1:
        create_dados()
    elif escolha == 2:
        consulta_dados()
    elif escolha == 3:
        update_dados()
    elif escolha == 4:
        delet_dados()
    elif escolha == 5:
        consulta_irrigacao_por_data()
    elif escolha == 6:
        break
    else:
        print("Opção inválida!")