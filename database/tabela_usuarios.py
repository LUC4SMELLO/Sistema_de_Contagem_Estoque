from database.banco_dados_principal import conectar_banco_dados_principal

from constants.bancos_dados import TABELA_USUARIOS


def criar_tabela_usuarios():

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_USUARIOS} (
    usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo VARCHAR(50),
    senha VARCHAR(50)
    )
    """
    )

    conexao.commit()
    conexao.close()
