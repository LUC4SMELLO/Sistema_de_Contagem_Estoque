import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_CONTAGENS, TABELA_CONTAGENS

def conectar_banco_dados_contagens():
    return sqlite3.connect(BANCO_DADOS_CONTAGENS)

def criar_banco_dados_contagens():
    
    conexao = conectar_banco_dados_contagens()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_CONTAGENS} (
    data VARCHAR(10),
    usuario_id VARCHAR(50),
    codigo_produto VARCHAR(10),
    quantidade_contada INT(8)
    )
    """
    )

    conexao.commit()
    conexao.close()