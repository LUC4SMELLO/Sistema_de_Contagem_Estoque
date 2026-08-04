from datetime import datetime

from database.banco_dados_principal import conectar_banco_dados_principal

from constants.bancos_dados import TABELA_RELATORIOS_ENTRADAS_TEMPORARIOS


class RelatoriosEntradasTemporarios():

    def __init__(self):
        pass

    @staticmethod
    def inserir_relatorio_temporario(usuario_id: int, dados_relatorio: dict):

        data_atual = datetime.now()
        data_atual_formatada = data_atual.strftime("%Y-%m-%d")

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()


        cursor.execute(
            f"""
            INSERT INTO {TABELA_RELATORIOS_ENTRADAS_TEMPORARIOS} (
                usuario_id,
                data_chegada,
                numero_carga,
                nota_fiscal,
                item,
                chave,
                codigo_produto,
                descricao,
                fabricacao,
                vencimento,
                fefo,
                pallet_danificado,
                vazamento,
                observacao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT (chave)
            DO UPDATE SET
                usuario_id        = excluded.usuario_id,
                data_chegada      = excluded.data_chegada,
                numero_carga      = excluded.numero_carga,
                nota_fiscal       = excluded.nota_fiscal,
                item              = excluded.item,
                codigo_produto    = excluded.codigo_produto,
                descricao         = excluded.descricao,
                fabricacao        = excluded.fabricacao,
                vencimento        = excluded.vencimento,
                fefo              = excluded.fefo,
                pallet_danificado = excluded.pallet_danificado,
                vazamento         = excluded.vazamento,
                observacao        = excluded.observacao
            """,
                (
                    usuario_id,
                    data_atual_formatada,
                    dados_relatorio["numero_carga"],
                    dados_relatorio["nota_fiscal"],
                    dados_relatorio["item"],
                    dados_relatorio["chave"],
                    dados_relatorio["codigo_produto"],
                    dados_relatorio["descricao"],
                    dados_relatorio["fabricacao"],
                    dados_relatorio["vencimento"],
                    dados_relatorio["fefo"],
                    dados_relatorio["pallet_danificado"],
                    dados_relatorio["vazamento"],
                    dados_relatorio["observacao"]
                )
        )

        conexao.commit()
        conexao.close()
