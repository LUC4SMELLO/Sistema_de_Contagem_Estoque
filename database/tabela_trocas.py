from database.banco_dados_principal import conectar_banco_dados_principal

from constants.bancos_dados import TABELA_TROCAS


def criar_tabela_trocas():

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_TROCAS} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        usuario_id VARCHAR(50),
        codigo_produto VARCHAR(10),
        quantidade INTEGER,
        situacao INTEGER
        )
        """
    )

    conexao.commit()
    conexao.close()
