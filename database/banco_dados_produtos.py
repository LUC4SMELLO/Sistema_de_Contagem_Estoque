import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_PRODUTOS, TABELA_PRODUTOS


def conectar_banco_dados_produtos():
    return sqlite3.connect(BANCO_DADOS_PRODUTOS)

def criar_banco_dados_produtos():
    
    conexao = conectar_banco_dados_produtos()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_PRODUTOS} (
    codigo_produto VARCHAR(10),
    descricao VARCHAR(50),
    quantidade INT(8)
    )
    """
    )

    conexao.commit()
    conexao.close()