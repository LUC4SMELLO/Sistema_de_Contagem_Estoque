import sqlite3

def conectar_banco_dados_contagem():
    return sqlite3.connect("TabelaContagem.db")

def criar_banco_dados_contagem():

    conexao = conectar_banco_dados_contagem()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaContagem (
    data VARCHAR(10),
    usuario VARCHAR(50),
    codigo_produto VARCHAR(10),
    quantidade_contada INT(8)
    )
    """
    )

    conexao.commit()
    conexao.close()
