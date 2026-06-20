from database.banco_dados_principal import conectar_banco_dados_principal

from constantes.bancos_dados import TABELA_CONTAGENS


def criar_tabela_contagens():

    conexao = conectar_banco_dados_principal()
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
