import re
from datetime import datetime


from database.banco_dados_principal import conectar_banco_dados_principal
from constants.bancos_dados import TABELA_RELATORIOS_ENTRADAS



def buscar_relatorio_entrada(carga: str):
    try:

        numero_carga, data_chegada = formatar_carga_selecionada(carga)

        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT
                data_chegada,
                item,
                codigo_produto,
                descricao,
                quantidade,
                data_fabricacao,
                data_vencimento,
                fefo,
                pallet_danificado,
                vazamento,
                observacao
            FROM {TABELA_RELATORIOS_ENTRADAS}
            WHERE numero_carga = ? AND data_chegada = ?
            ORDER BY item AND numero_carga ASC
            """,
            (numero_carga, data_chegada),
        )

        dados = cursor.fetchall()

        conexao.close()


        colunas = [coluna[0] for coluna in cursor.description]
        relatorio_completo = [dict(zip(colunas, linha)) for linha in dados]


        for relatorio in relatorio_completo:

            data_estoque = buscar_data_estoque(relatorio["codigo_produto"], relatorio["data_vencimento"])
            shelf_life = buscar_shelf_life(relatorio["data_vencimento"], relatorio["data_fabricacao"])
            dias_para_vencimento = buscar_dias_para_vencimento(relatorio["data_vencimento"], relatorio["data_chegada"])
            dias_para_vencimento_porcentagem = buscar_dias_para_vencimento_porcentagem(dias_para_vencimento, shelf_life)


            relatorio["data_fabricacao"] = formatar_data(relatorio["data_fabricacao"])
            relatorio["data_vencimento"] = formatar_data(relatorio["data_vencimento"])

            relatorio["data_estoque"] = data_estoque
            relatorio["shelf_life"] = shelf_life
            relatorio["dias_para_vencimento"] = dias_para_vencimento
            relatorio["dias_para_vencimento_porcentagem"] = f"{dias_para_vencimento_porcentagem}%"


        return numero_carga, relatorio_completo

    except Exception:
        return ""




def buscar_data_estoque(codigo_produto: str, data_vencimento: str):
    try:
        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT codigo_produto, data_vencimento
            FROM {TABELA_RELATORIOS_ENTRADAS}
            WHERE codigo_produto = ?
            ORDER BY data_chegada ASC
            """, (codigo_produto,)
        )

        resultado = cursor.fetchone()

        conexao.close()
        
        if not resultado:
            return data_vencimento

        return formatar_data(resultado[1])
    
    except Exception:
        return False


def buscar_shelf_life(data_vencimento: str, data_fabricacao: str):
    try:
        data_vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d")
        data_fabricacao = datetime.strptime(data_fabricacao, "%Y-%m-%d")

        diferenca = data_vencimento - data_fabricacao

        shelf_life = diferenca.days

        return shelf_life
    
    except Exception:
        return ""


def buscar_dias_para_vencimento(data_vencimento: str, data_chegada: str):
    try:
        data_vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d")
        data_chegada = datetime.strptime(data_chegada, "%Y-%m-%d")

        diferenca = data_vencimento - data_chegada

        dias_para_vencimento = diferenca.days

        return dias_para_vencimento

    except Exception:
        return ""

def buscar_dias_para_vencimento_porcentagem(dias_para_vencimento: int, shelf_life: int):
    try:    
        porcentagem_restante = (dias_para_vencimento / shelf_life) * 100
        
        return round(porcentagem_restante, 2)
    
    except Exception:
        return ""






        

def buscar_relatorios_inseridos():

    try:
        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT DISTINCT numero_carga, data_chegada
            FROM {TABELA_RELATORIOS_ENTRADAS}
            ORDER BY data_chegada, numero_carga ASC
            """
        )

        resultado = list(cursor.fetchall())

        resultado_formatado = [(id_val, datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')) for id_val, data in resultado]


        conexao.close()

        return resultado_formatado

    except Exception:
        return ""



def formatar_carga_selecionada(data_chegada: str):
    try:
        padrao = r"(\d+)\s+(\d{2}/\d{2}/\d{4})"
    
        resultado = re.search(padrao, data_chegada)

        if resultado:
            numero_carga = resultado.group(1)
            data = resultado.group(2)

            objeto_data = datetime.strptime(data, "%d/%m/%Y")
            data_formatada = objeto_data.strftime("%Y-%m-%d")

            return numero_carga, data_formatada

    except Exception:
        return ""


def formatar_data(data: str):
    """
    Formata uma data no formato americano para o formato brasileiro.

    Parameters
    ----------
        data: str
            A data que será formatada.
    """

    try:
        objeto_data = datetime.strptime(data, "%Y-%m-%d")
        data_formatada = objeto_data.strftime("%d/%m/%Y")

        return data_formatada
    
    except Exception:
        return ""
