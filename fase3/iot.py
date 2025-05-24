from banco import BancoDeDados

def salvar_leitura_esp32(tipo, valor):
    db = BancoDeDados(user="RM560146", password="240890", host="ORACLE.FIAP.COM.BR", port=1521, service_name="ORCL")
    db.inserir_leitura_sensor(tipo, valor)
    db.fechar()
