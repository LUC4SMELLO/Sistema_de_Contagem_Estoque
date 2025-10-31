from database.banco_dados_contagens_temporarias import conectar_banco_dados_contagens_temporaria

from backend.constantes.bancos_dados import TABELA_CONTAGENS_TEMPORARIAS

class ContagemTemporaria:
    """
    Representa a contagem temporária feita pelo usuário.

    Attributes
    ----------
        data
            Data da contagem.
        usuario_id
            Id do usuário.
        codigo_produto
            Código produto.
        quantidade_contada
            Quantidade Contada.
    """

    def __init__(self, data, usuario_id, codigo_produto, quantidade_contada):
        """
        Inicializa uma nova contagem temporária.

        Parameters
        ----------
            data
                A data da contagem.
            usuario_id
                O id do usuário.
            codigo_produto
                O código do produto.
            quantidade_contada
                A quantidade contada.
        """

        self.data = data
        self.usuario_id = usuario_id
        self.codigo_produto = codigo_produto
        self.quantidade_contada = quantidade_contada

    def inserir_contagem(self):
        """
        Insere uma nova contagem temporária no banco de dados.
        """

        conexao = conectar_banco_dados_contagens_temporaria()
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
        """
        Exclui a contagem temporária do banco de dados.

        Parameters
        ----------
            usuario_id
                O id do usuário.
            data
                A data da contagem temporária.
        """

        conexao = conectar_banco_dados_contagens_temporaria()
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
        """
        Carrega a contagem temporária do banco de dados.

        Parameters
        ----------
            usuario_id
                O id do usuário.
            data
                A data da contagem temporária.

        Returns
        -------
            Uma lista de tuplas.
        """

        conexao = conectar_banco_dados_contagens_temporaria()
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
