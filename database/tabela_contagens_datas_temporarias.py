from database.banco_dados_principal import conectar_banco_dados_principal

from constants.bancos_dados import TABELA_CONTAGENS_DATAS_TEMPORARIAS


def criar_tabela_contagens_datas_temporarias():

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_CONTAGENS_DATAS_TEMPORARIAS} (
            data_contagem TEXT,
            usuario_id VARCHAR(50),
            rua INTEGER,
            bloco INTEGER,
            coluna TEXT,
            nivel INTEGER,
            chave TEXT PRIMARY KEY,
            codigo_produto VARCHAR(10),
            data_fabricacao TEXT,
            data_validade TEXT
        )
        """
    )

    conexao.commit()
    conexao.close()
