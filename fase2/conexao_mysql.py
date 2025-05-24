import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='seu_banco_de_dados'
    )
