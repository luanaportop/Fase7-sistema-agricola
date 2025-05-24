import oracledb

class BancoDeDados:
    def __init__(self, user, password, host, port, service_name):
        dsn = oracledb.makedsn(host, port, service_name=service_name)
        self.connection = oracledb.connect(user=user, password=password, dsn=dsn, mode=oracledb.DEFAULT_AUTH)
        print("Conectado ao Oracle!")

    def inserir_leitura_sensor(self, tipo_sensor, valor):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO Sensores (tipo_sensor, valor) VALUES (:tipo_sensor, :valor)"
            cursor.execute(sql, {"tipo_sensor": tipo_sensor, "valor": valor})
        self.connection.commit()
        print(f"Leitura do sensor {tipo_sensor} inserida com valor {valor}.")

    def registrar_irrigacao(self, status):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO Irrigacao (status) VALUES (:status)"
            cursor.execute(sql, {"status": status})
        self.connection.commit()
        print(f"Irrigação {status} registrada.")

    def registrar_historico(self, id_sensor, id_irrigacao):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO Historico_Irrigacao (id_sensor, id_irrigacao) VALUES (:id_sensor, :id_irrigacao)"
            cursor.execute(sql, {"id_sensor": id_sensor, "id_irrigacao": id_irrigacao})
        self.connection.commit()
        print("Histórico de irrigação registrado.")

    def consultar_historico(self):
        with self.connection.cursor() as cursor:
            sql = """
                SELECT h.data_registro, s.tipo_sensor, s.valor, i.status
                FROM Historico_Irrigacao h
                JOIN Sensores s ON h.id_sensor = s.id_sensor
                JOIN Irrigacao i ON h.id_irrigacao = i.id_irrigacao
                ORDER BY h.data_registro DESC
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

    def atualizar_leitura_sensor(self, id_sensor, novo_valor):
        with self.connection.cursor() as cursor:
            sql = "UPDATE Sensores SET valor = :novo_valor WHERE id_sensor = :id_sensor"
            cursor.execute(sql, {"novo_valor": novo_valor, "id_sensor": id_sensor})
        self.connection.commit()
        print(f"Leitura do sensor ID {id_sensor} atualizada para valor {novo_valor}.")

    def deletar_historico(self, id_historico):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM Historico_Irrigacao WHERE id_historico = :id_historico"
            cursor.execute(sql, {"id_historico": id_historico})
        self.connection.commit()
        print(f"Registro de histórico ID {id_historico} deletado.")

    def fechar(self):
        self.connection.close()
        print("Conexão encerrada.")
