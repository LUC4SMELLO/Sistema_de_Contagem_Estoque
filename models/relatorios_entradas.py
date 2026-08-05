from datetime import datetime

from database.banco_dados_principal import conectar_banco_dados_principal
from constants.bancos_dados import TABELA_RELATORIOS_ENTRADAS



class RelatoriosEntradas():

    def __init__(self):
        pass

    @staticmethod
    def inserir_relatorio(usuario_id: int, dados_relatorio: dict):

        data_atual = datetime.now()
        data_atual_formatada = data_atual.strftime("%Y-%m-%d")

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        for i in range(len(dados_relatorio)):
            cursor.execute(
                f"""
                INSERT INTO {TABELA_RELATORIOS_ENTRADAS} (
                usuario_id,
                data_chegada,
                numero_carga,
                nota_fiscal,
                motorista,
                local,
                item,
                codigo_produto,
                descricao,
                fabricacao,
                vencimento,
                fefo,
                pallet_danificado,
                vazamento,
                observacao
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        usuario_id,
                        data_atual_formatada,
                        dados_relatorio[i]["numero_carga"],
                        dados_relatorio[i]["nota_fiscal"],
                        dados_relatorio[i]["motorista"],
                        dados_relatorio[i]["local"],
                        dados_relatorio[i]["item"],
                        dados_relatorio[i]["codigo_produto"],
                        dados_relatorio[i]["descricao"],
                        dados_relatorio[i]["fabricacao"],
                        dados_relatorio[i]["vencimento"],
                        dados_relatorio[i]["fefo"],
                        dados_relatorio[i]["pallet_danificado"],
                        dados_relatorio[i]["vazamento"],
                        dados_relatorio[i]["observacao"]
                    )
            )

        conexao.commit()
        conexao.close()


