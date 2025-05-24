import oracledb
import pandas as pd

# Conexão com banco Oracle
def conectar():
    try:
        conn = oracledb.connect(
            user='RM560146',
            password='240890',
            dsn='oracle.fiap.com.br:1521/ORCL'
        )
        return conn
    except Exception as e:
        print("Erro ao conectar:", e)
        return None

# Função para inserir dados
def inserir_sensor(ph, fosforo, potassio, umidade, temperatura):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = """
        INSERT INTO t_sensor (id_sensor, leitura_ph, leitura_fosforo_p, leitura_potassio_k, leitura_umidade, leitura_temperatura)
        VALUES (SENSOR_SEQ.NEXTVAL, :1, :2, :3, :4, :5)
        """
        cursor.execute(sql, (ph, fosforo, potassio, umidade, temperatura))
        conn.commit()
        conn.close()

# Leitura dos dados
def listar_dados():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM t_sensor ORDER BY data_hora DESC")
        dados = cursor.fetchall()
        colunas = [i[0] for i in cursor.description]
        df = pd.DataFrame(dados, columns=colunas)
        conn.close()
        return df
