from .banco import BancoDeDados

def conectar_banco():
    return BancoDeDados(user="RM560146", password="240890", host="ORACLE.FIAP.COM.BR", port=1521, service_name="ORCL")

def inserir_leitura(tipo, valor):
    db = conectar_banco()
    db.inserir_leitura_sensor(tipo, valor)
    db.fechar()

def registrar_irrigacao(status):
    db = conectar_banco()
    db.registrar_irrigacao(status)
    db.fechar()

def registrar_historico(id_sensor, id_irrigacao):
    db = conectar_banco()
    db.registrar_historico(id_sensor, id_irrigacao)
    db.fechar()

def atualizar_leitura(id_sensor, novo_valor):
    db = conectar_banco()
    db.atualizar_leitura_sensor(id_sensor, novo_valor)
    db.fechar()

def deletar_historico(id):
    db = conectar_banco()
    db.deletar_historico(id)
    db.fechar()

def obter_historico():
    db = conectar_banco()
    historico = db.consultar_historico()
    db.fechar()
    return historico
