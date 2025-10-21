from database.banco_dados_produtos import conectar_banco_dados_produtos

from backend.constantes.bancos_dados import TABELA_PRODUTOS


class Produto:
    """
    Representa um produto.

    Attributes
    ----------
        codigo_produto
            O código do produto.
        descricao
            A descrição do produto (nome).
        quantidade
            O estoque do produto.
    """


    def __init__(self, codigo_produto, descricao, quantidade):
        """
        Inicializa um novo produto.

        Parameters
        ----------
            codigo_produto
                O código do produto.
            descricao
                A descrição do produto (nome).
            quantidade
                O estoque do produto.
        """

        self.codigo_produto = codigo_produto
        self.descricao = descricao
        self.estoque = quantidade

    def inserir_produto(self):
        """
        Insere um novo produto no banco de dados.
        """

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
        """
        Exclui um produto do banco de dados.

        Parameters
        ----------
            codigo_produto
                O código do produto.
        """

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
        """
        Busca um produto.

        Parameters
        ----------
            codigo_produto
                O código do produto.

        Returns
        -------
            Uma lista de tuplas.

        """

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