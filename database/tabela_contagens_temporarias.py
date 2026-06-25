from database.banco_dados_principal import conectar_banco_dados_principal

from constants.bancos_dados import TABELA_CONTAGENS_TEMPORARIAS


def criar_tabela_contagens_temporarias():

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_CONTAGENS_TEMPORARIAS} (
    data TEXT,
    usuario_id VARCHAR(50),
    codigo_produto VARCHAR(10),
    quantidade_contada INT(8)
    )
    """
    )

    conexao.commit()
    conexao.close()
