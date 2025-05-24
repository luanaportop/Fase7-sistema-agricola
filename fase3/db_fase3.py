# fase3/db_fase3.py

import oracledb
from datetime import datetime

class BancoDeDados:
    def __init__(self, user, password, host, port, service_name):
        dsn = f"{host}:{port}/{service_name}"
        self.conexao = oracledb.connect(user=user, password=password, dsn=dsn)
        self.cursor = self.conexao.cursor()

    def inserir_leitura_sensor(self, tipo_sensor, valor):
        self.cursor.execute("""
            INSERT INTO T_SENSOR (id_sensor, tipo_sensor, valor_sensor, data_hora)
            VALUES (T_SENSOR_SEQ.NEXTVAL, :1, :2, SYSTIMESTAMP)
        """, (tipo_sensor, valor))
        self.conexao.commit()

    def registrar_irrigacao(self, status):
        self.cursor.execute("""
            INSERT INTO T_IRRIGACAO (id_irrigacao, status_irrigacao, data_hora)
            VALUES (T_IRRIGACAO_SEQ.NEXTVAL, :1, SYSTIMESTAMP)
        """, (status,))
        self.conexao.commit()

    def registrar_historico(self, id_sensor, id_irrigacao):
        self.cursor.execute("""
            INSERT INTO T_HISTORICO (id_historico, id_sensor, id_irrigacao, data_hora)
            VALUES (T_HISTORICO_SEQ.NEXTVAL, :1, :2, SYSTIMESTAMP)
        """, (id_sensor, id_irrigacao))
        self.conexao.commit()

    def atualizar_leitura_sensor(self, id_sensor, novo_valor):
        self.cursor.execute("""
            UPDATE T_SENSOR SET valor_sensor = :1 WHERE id_sensor = :2
        """, (novo_valor, id_sensor))
        self.conexao.commit()

    def deletar_historico(self, id_historico):
        self.cursor.execute("DELETE FROM T_HISTORICO WHERE id_historico = :1", (id_historico,))
        self.conexao.commit()

    def consultar_historico(self):
        self.cursor.execute("""
            SELECT h.data_hora, s.tipo_sensor, s.valor_sensor, i.status_irrigacao
            FROM T_HISTORICO h
            JOIN T_SENSOR s ON h.id_sensor = s.id_sensor
            JOIN T_IRRIGACAO i ON h.id_irrigacao = i.id_irrigacao
            ORDER BY h.data_hora DESC
        """)
        return self.cursor.fetchall()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()
