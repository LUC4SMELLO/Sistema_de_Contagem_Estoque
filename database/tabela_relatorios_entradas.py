from database.banco_dados_principal import conectar_banco_dados_principal

from constants.bancos_dados import TABELA_RELATORIOS_ENTRADAS


def criar_tabela_relatorios_entrada():

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_RELATORIOS_ENTRADAS} (
        usuario_id VARCHAR(50),
        data_chegada TEXT,
        numero_carga INTEGER,
        nota_fiscal VARCHAR(50),
        item INTEGER,
        codigo_produto VARCHAR(10),
        descricao VARCHAR(150),
        fabricacao TEXT,
        vencimento TEXT,
        fefo INTEGER,
        pallet_danificado INTEGER,
        vazamento INTEGER,
        observacao VARCHAR(250)
        )
        """
    )

    conexao.commit()
    conexao.close()
