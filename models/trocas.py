from datetime import datetime

from database.banco_dados_principal import conectar_banco_dados_principal

from constants.bancos_dados import TABELA_TROCAS


class Trocas():
    """
    Representa a troca feita pelo usuário.
    """

    @staticmethod
    def inserir_troca(usuario_id: int, troca: dict):
        "Insere uma nova troca no banco de dados."

        data_atual = datetime.now()
        data_atual_formatada = data_atual.strftime("%Y-%m-%d %H:%M")

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            INSERT INTO {TABELA_TROCAS} (
            data,
            usuario_id,
            codigo_produto,
            quantidade,
            situacao
            )
            VALUES (?, ?, ?, ?, ?)
            """, (
                data_atual_formatada,
                usuario_id,
                troca["codigo_produto"],
                troca["quantidade"],
                0
            )
        )

        conexao.commit()
        conexao.close()


    @staticmethod
    def excluir_troca(id: int):
        """
        Exclui uma troca no banco de dados.

        Parameters
        ----------
            id: int
                O id da troca.

        Returns
        -------
            None
        """

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            DELETE FROM {TABELA_TROCAS}
            WHERE id = ?
            """, (id, )
        )

        conexao.commit()
        conexao.close()


    @staticmethod
    def buscar_troca(id: int):
        """
        Busca a troca com base no id.

        Parameters
        ----------
            id: int
                O id da troca.

        Returns
        -------
            codigo_produto: str
                O código do produto.
            quantidade: str
                A quantidade.
        """

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT codigo_produto, quantidade
            FROM {TABELA_TROCAS}
            WHERE id = ? AND situacao = 0
            """, (id, )
        )

        resultado = cursor.fetchall()

        conexao.close()

        if not resultado:
            return "", ""

        codigo_produto, quantidade = resultado[0]

        return codigo_produto, quantidade
