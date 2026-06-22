from database.banco_dados_principal import conectar_banco_dados_principal

from constantes.bancos_dados import TABELA_CONTAGENS_DATAS_TEMPORARIAS, TABELA_CONTAGENS_DATAS


def indexar_contagem_datas(contagem_datas):
    
    contagem_para_carregar = {}
    for registro in contagem_datas:
        (
            _data_contagem,
            _usuario_id,
            rua,
            bloco,
            coluna,
            nivel,
            codigo_produto,
            data_fabricacao,
            data_validade
        ) = registro

        contagem_para_carregar[(str(rua), str(bloco), str(coluna), str(nivel))] = {
            "codigo": codigo_produto,
            "data_fabricacao": data_fabricacao,
            "data_validade": data_validade
        }

    return contagem_para_carregar


def buscar_contagem_datas_temporarias(usuario_id: int, data: str):

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        SELECT data_contagem, usuario_id, rua, bloco,
            coluna, nivel, codigo_produto, data_fabricacao, data_validade
        FROM {TABELA_CONTAGENS_DATAS_TEMPORARIAS}
        WHERE usuario_id = ? AND data_contagem = ?
        ORDER BY data_contagem, rua, bloco, coluna, nivel
        """, (usuario_id, data)
    )

    contagens_temporarias = cursor.fetchall()

    conexao.close()
    
    return contagens_temporarias
    

def buscar_ultima_contagem_datas():

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        SELECT data_contagem, usuario_id, rua, bloco,
            coluna, nivel, codigo_produto, data_fabricacao, data_validade
        FROM {TABELA_CONTAGENS_DATAS}
        WHERE data_contagem = (
            SELECT MAX(data_contagem)
            FROM {TABELA_CONTAGENS_DATAS}
        )
        ORDER BY data_contagem, rua, bloco, coluna, nivel
        """
    )

    ultima_contagem = cursor.fetchall()

    conexao.close()

    return ultima_contagem


def selecionar_contagem_datas_para_carregar(usuario_id, data):

    contagem_datas_temporarias = buscar_contagem_datas_temporarias(usuario_id, data)
    if contagem_datas_temporarias:
        contagem_indexada = indexar_contagem_datas(contagem_datas_temporarias)

        return contagem_indexada
    
    ultima_contagem_datas = buscar_ultima_contagem_datas()
    if ultima_contagem_datas:
        contagem_indexada = indexar_contagem_datas(ultima_contagem_datas)

        return contagem_indexada

    return {}