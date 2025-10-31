import sqlite3

from backend.constantes.bancos_dados import BANCO_DADOS_CONTAGENS_TEMPORARIAS, TABELA_CONTAGENS_TEMPORARIAS

def conectar_banco_dados_contagens_temporaria():
    return sqlite3.connect(BANCO_DADOS_CONTAGENS_TEMPORARIAS)

def criar_banco_dados_contagens_temporarias():

    conexao = conectar_banco_dados_contagens_temporaria()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_CONTAGENS_TEMPORARIAS} (
    data VARCHAR(10),
    usuario_id VARCHAR(50),
    codigo_produto VARCHAR(10),
    quantidade_contada INT(8)
    )
    """
    )

    conexao.commit()
    conexao.close()
