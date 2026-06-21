from typing import List, Tuple

from datetime import datetime

from database.banco_dados_principal import conectar_banco_dados_principal

from constantes.bancos_dados import TABELA_CONTAGENS_DATAS


class ContagensDatas():

    def __init__(self):
        pass

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
        data_atual_formatada = data_atual.strftime("%Y-%m-%d %H:%M:%S")

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        for i in range(len(contagens)):
            cursor.execute(
                f"""
                INSERT INTO {TABELA_CONTAGENS_DATAS} (
                data,
                usuario_id,
                rua,
                bloco,
                coluna,
                nivel,
                codigo_produto,
                data_contada
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (  
                    data_atual_formatada,
                    usuario_id,
                    contagens[i]["rua"],
                    contagens[i]["bloco"],
                    contagens[i]["coluna"],
                    contagens[i]["nivel"],
                    contagens[i]["codigo_produto"],
                    contagens[i]["data_contada"]
                )
            )

        conexao.commit()
        conexao.close()


    @staticmethod
    def buscar_ultima_contagem():

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT *
            FROM {TABELA_CONTAGENS_DATAS}
            WHERE data = (
                SELECT MAX(data)
                FROM {TABELA_CONTAGENS_DATAS}
            )
            ORDER BY data, rua, bloco, coluna, nivel
            """
        )

        ultima_contagem = cursor.fetchall()

        conexao.close()


        contagem_anterior = {}
        for registro in ultima_contagem:
            (
                data,
                usuario_id,
                rua,
                bloco,
                coluna,
                nivel,
                codigo_produto,
                data_contada
            ) = registro

            contagem_anterior[(str(rua), str(bloco), str(coluna), str(nivel))] = {
                "codigo": codigo_produto,
                "data": data_contada
            }

        return contagem_anterior
