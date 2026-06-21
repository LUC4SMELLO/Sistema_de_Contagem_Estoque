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