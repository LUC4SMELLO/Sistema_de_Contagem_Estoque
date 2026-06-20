import sqlite3

from constantes.bancos_dados import BANCO_DADOS_PRINCIPAL


def conectar_banco_dados_principal():
    return sqlite3.connect(BANCO_DADOS_PRINCIPAL)
