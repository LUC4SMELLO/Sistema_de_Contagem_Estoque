from database.banco_dados_produtos import conectar_banco_dados_produtos

from backend.constantes.bancos_dados import TABELA_PRODUTOS


class Produto:
    def __init__(self, codigo_produto, descricao, quantidade):
        self.codigo_produto = codigo_produto
        self.descricao = descricao
        self.estoque = quantidade

    def inserir_produto(self):

        conexao = conectar_banco_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        INSERT INTO {TABELA_PRODUTOS} (
        codigo_produto,
        descricao,
        quantidade
        )
        VALUES (?, ?, ?)
        """, (self.codigo_produto, self.descricao, self.estoque)
        )
        
        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_produto(codigo_produto):

        conexao = conectar_banco_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        DELETE FROM {TABELA_PRODUTOS}
        WHERE codigo_produto = ?
        """, (codigo_produto,)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar_produto(codigo_produto):

        conexao = conectar_banco_dados_produtos()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        SELECT * FROM {TABELA_PRODUTOS}
        WHERE codigo_produto = ?
        """, (codigo_produto,)
        )

        resultado = cursor.fetchall()

        conexao.commit()
        conexao.close()

        return resultado