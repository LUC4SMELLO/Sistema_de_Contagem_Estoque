from typing import List, Tuple

from datetime import datetime

from database.banco_dados_contagens import conectar_banco_dados_contagens

from backend.constantes.bancos_dados import TABELA_CONTAGENS

class Contagens():
    """
    Representa a contagem final feita pelo usuário.

    Attributes
    ---------
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
        Inicializa uma nova contagem.

        Parameters
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

        self.data = data
        self.usuario_id = usuario_id
        self.codigo_produto = codigo_produto
        self.quantidade_contada = quantidade_contada

    def inserir_contagem(self):
        """
        Insere uma nova contagem no banco de dados.
        """

        conexao = conectar_banco_dados_contagens()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        INSERT INTO {TABELA_CONTAGENS} (
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
    def inserir_contagens(usuario_id: int, contagens: List[Tuple]):
        """
        Insere uma nova contagem no banco de dados.

        Parameters
        ----------
            usuario_id: int
                O id do usuário.
            contagens: List[Tuple]
                Uma lista de tuplas com as contagens.

        Returns
        -------
            None
        """
        
        data_atual = datetime.now()
        data_atual_formatada = data_atual.strftime("%d/%m/%Y, %H:%M")

        conexao = conectar_banco_dados_contagens()
        cursor = conexao.cursor()

        for i in range(len(contagens)):
            cursor.execute(
                f"""
                INSERT INTO {TABELA_CONTAGENS} (
                data,
                usuario_id,
                codigo_produto,
                quantidade_contada
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    data_atual_formatada,
                    usuario_id,
                    contagens[i]["codigo"],
                    contagens[i]["quantidade"]
                )
            )

        conexao.commit()
        conexao.close()


    @staticmethod
    def excluir_contagem(usuario_id, data):
        """
        Exclui a contagem do banco de dados.

        Parameters
        ----------
            usuario_id
                O id do usuário.
            data
                A data da contagem temporária.
        """

        conexao = conectar_banco_dados_contagens()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        DELETE FROM {TABELA_CONTAGENS}
        WHERE usuario_id = ? AND data = ?
        """, (usuario_id, data)
        )

        conexao.commit()
        conexao.close()