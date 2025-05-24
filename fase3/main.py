from banco import BancoDeDados

def main():
    # Configura sua conexão aqui
    db = BancoDeDados(user="RM560146", password="240890", host="ORACLE.FIAP.COM.BR", port=1521, service_name="ORCL")

    # Inserir leitura de sensor
    db.inserir_leitura_sensor("Umidade", 55)

    # Registrar irrigação
    db.registrar_irrigacao("Ligado")

    # Registrar histórico (coloque IDs válidos)
    db.registrar_historico(id_sensor=1, id_irrigacao=1)

    # Atualizar leitura
    db.atualizar_leitura_sensor(1, 60)

    # Deletar histórico
    db.deletar_historico(1)

    # Consultar e mostrar histórico
    historico = db.consultar_historico()
    for registro in historico:
        print(f"Data: {registro[0]}, Sensor: {registro[1]}, Valor: {registro[2]}, Status Irrigação: {registro[3]}")

    # Fechar conexão
    db.fechar()

if __name__ == "__main__":
    main()
