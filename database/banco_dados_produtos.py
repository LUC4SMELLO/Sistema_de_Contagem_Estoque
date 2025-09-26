import sqlite3

def conectar_banco_dados_produtos():
    return sqlite3.connect("TabelaProdutos.db")

def criar_banco_dados_produtos():
    
    conexao = conectar_banco_dados_produtos()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS TabelaProdutos (
    codigo_produto VARCHAR(10),
    descricao VARCHAR(50),
    quantidade INT(8)
    )
    """
    )

    conexao.commit()
    conexao.close()