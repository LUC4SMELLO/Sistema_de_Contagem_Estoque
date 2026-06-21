from database.banco_dados_principal import conectar_banco_dados_principal

from constantes.bancos_dados import TABELA_CONTAGENS_DATAS


def criar_tabela_contagens_datas():

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_CONTAGENS_DATAS} (
        data VARCHAR(10),
        usuario_id VARCHAR(50),
        rua VARCHAR(10),
        bloco VARCHAR(10),
        coluna VARCHAR(10),
        nivel VARCHAR(10),
        codigo_produto VARCHAR(10),
        data_contada VARCHAR(10)
        )
        """
    )

    conexao.commit()
    conexao.close()
