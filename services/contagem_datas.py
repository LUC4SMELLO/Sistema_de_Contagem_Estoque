from datetime import date

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


def mesclar_contagens(contagem_base_lista, contagem_nova_lista):
    """
    Recebe duas listas do banco de dados, indexa os registros por posição
    e retorna o resultado final unificado em um dicionário.
    """

    # INDEXA A CONTAGEM ANTIGA
    resultado = indexar_contagem_datas(contagem_base_lista)

    # INDEXA A CONTAGEM NOVA (TEMPORÁRIA) POR CIMA DA BASE
    # SUBSTITUI AUTOMATICAMENTE OS DADOS SE A POSIÇÃO FOR IDÊNTICA
    for registro in contagem_nova_lista:
        (
            _data_contagem, _usuario_id, rua, bloco, coluna, nivel,
            codigo_produto, data_fabricacao, data_validade
        ) = registro
        
        chave_posicao = (str(rua), str(bloco), str(coluna), str(nivel))
        
        resultado[chave_posicao] = {
            "codigo": codigo_produto,
            "data_fabricacao": data_fabricacao,
            "data_validade": data_validade
        }
        
    return resultado


def buscar_contagem_datas_temporarias(usuario_id: int):

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%Y-%m-%d")

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        SELECT data_contagem, usuario_id, rua, bloco,
            coluna, nivel, codigo_produto, data_fabricacao, data_validade
        FROM {TABELA_CONTAGENS_DATAS_TEMPORARIAS}
        WHERE usuario_id = ? AND data_contagem = ?
        ORDER BY data_contagem, rua, bloco, coluna, nivel
        """, (usuario_id, data_atual_formatada)
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


def selecionar_contagem_datas_para_carregar(usuario_id):

    contagem_datas_temporarias = buscar_contagem_datas_temporarias(usuario_id)
    ultima_contagem_datas = buscar_ultima_contagem_datas()

    if contagem_datas_temporarias and ultima_contagem_datas:
        contagem_mesclada = mesclar_contagens(ultima_contagem_datas, contagem_datas_temporarias)
        return contagem_mesclada

    elif contagem_datas_temporarias:
        contagem_indexada = indexar_contagem_datas(contagem_datas_temporarias)
        return contagem_indexada
    
    elif ultima_contagem_datas:
        contagem_indexada = indexar_contagem_datas(ultima_contagem_datas)
        return contagem_indexada

    else:
        return {}
