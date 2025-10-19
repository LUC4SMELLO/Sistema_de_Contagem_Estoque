from database.banco_dados_contagem import conectar_banco_dados_contagem

from backend.constantes.bancos_dados import TABELA_CONTAGENS_TEMPORARIAS

class Contagem:
    def __init__(self, data, usuario_id, codigo_produto, quantidade_contada):
        self.data = data
        self.usuario_id = usuario_id
        self.codigo_produto = codigo_produto
        self.quantidade_contada = quantidade_contada

    def inserir_contagem(self):

        conexao = conectar_banco_dados_contagem()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        INSERT INTO {TABELA_CONTAGENS_TEMPORARIAS} (
        data,
        usuario_id,
        codigo_produto,
        quantidade_contada
        )
        VALUES (?, ?, ?, ?)
        """, (self.data, self.usuario_id, self.codigo_produto, self.quantidade_contada)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_contagem(usuario_id, data):

        conexao = conectar_banco_dados_contagem()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        DELETE FROM {TABELA_CONTAGENS_TEMPORARIAS}
        WHERE usuario_id = ? AND data = ?
        """, (usuario_id, data)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def carregar_contagem(usuario_id, data):

        conexao = conectar_banco_dados_contagem()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        SELECT * FROM {TABELA_CONTAGENS_TEMPORARIAS}
        WHERE usuario_id = ? AND data = ?
        """, (usuario_id, data)
        )

        resultado = cursor.fetchall()

        conexao.close()

        contagens = [{"produto_id": linha[2], "quantidade": linha[3]} for linha in resultado]

        return contagens
