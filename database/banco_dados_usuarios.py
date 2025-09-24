import sqlite3

def conectar_banco_dados_usuarios():

    return sqlite3.connect("TabelaUsuarios.db")

def criar_banco_dados_usuarios():

    conexao = conectar_banco_dados_usuarios()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaUsuarios (
    nome_completo VARCHAR(50),
    senha VARCHAR(50)
    )
    """
    )

    conexao.commit()
    conexao.close()
