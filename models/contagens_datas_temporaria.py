from database.banco_dados_principal import conectar_banco_dados_principal
from constantes.bancos_dados import TABELA_CONTAGENS_DATAS_TEMPORARIAS


class ContagensDatasTemporaria():

    def __init__(self):
        pass

    @staticmethod
    def inserir_contagem(
        data_contagem,
        usuario_id,
        rua,
        bloco,
        coluna,
        nivel,
        chave,
        codigo_produto,
        data_fabricacao,
        data_validade
    ):
        """
        Insere uma nova contagem temporária no banco de dados.
        """

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            INSERT INTO {TABELA_CONTAGENS_DATAS_TEMPORARIAS} (
            data_contagem,
            usuario_id,
            rua,
            bloco,
            coluna,
            nivel,
            chave,
            codigo_produto,
            data_fabricacao,
            data_validade
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(chave)
            DO UPDATE SET
                data_contagem    = excluded.data_contagem,
                usuario_id       = excluded.usuario_id,
                rua              = excluded.rua,
                bloco            = excluded.bloco,
                coluna           = excluded.coluna,
                nivel            = excluded.nivel,
                codigo_produto   = excluded.codigo_produto,
                data_fabricacao  = excluded.data_fabricacao,
                data_validade    = excluded.data_validade

            """,
                (
                    data_contagem,
                    usuario_id,
                    rua,
                    bloco,
                    coluna,
                    nivel,
                    chave,
                    codigo_produto,
                    data_fabricacao,
                    data_validade,
                )
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_contagem(usuario_id):
        """
        Exclui uma contagem do banco de dados.
        """

        conexao = None

        try:
            conexao = conectar_banco_dados_principal()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                DELETE FROM {TABELA_CONTAGENS_DATAS_TEMPORARIAS}
                WHERE usuario_id = ?
                """, (usuario_id,)
            )

            conexao.commit()

        except Exception as erro:
            print("Erro ao excluir contagem data temporária: ", erro)
            return
        
        finally:
            if conexao:
                conexao.close()
