import os
from typing import List, Tuple

from datetime import datetime

import pandas as pd

from constants.paths import EXPORT_CONTAGEM_DATAS

from models.contagens_datas import ContagensDatas
from models.contagens_datas_temporaria import ContagensDatasTemporaria


def salvar_arquivo_contagem_datas(contagens: List[Tuple], usuario_id) -> None:
    """
    Salva um arquivo .csv com a contagem de datas feita pelo usuário.

    Parameters
    ----------
        contagens
            Uma lista de tuplas com as contagens.

    Returns
    -------
        None
    """

    try:

        data_atual = datetime.now()
        data_atual_formatada = data_atual.strftime("%d-%m-%Y_%H-%M-%S")

        CAMINHO_SALVAR_ARQUIVO_CSV = EXPORT_CONTAGEM_DATAS / f"contagem_datas_{data_atual_formatada}.csv"

        contagem_data = pd.DataFrame(contagens)

        contagem_data["data_validade"] = pd.to_datetime(contagem_data["data_validade"])
        contagem_data["data_fabricacao"] = pd.to_datetime(contagem_data["data_fabricacao"])

        contagem_data["data_validade"] = contagem_data["data_validade"].dt.strftime('%d/%m/%Y')
        contagem_data["data_fabricacao"] = contagem_data["data_fabricacao"].dt.strftime('%d/%m/%Y')

        contagem_data.to_csv(CAMINHO_SALVAR_ARQUIVO_CSV, index=False)


        if not os.path.exists(CAMINHO_SALVAR_ARQUIVO_CSV) or os.path.getsize(CAMINHO_SALVAR_ARQUIVO_CSV) == 0:
            raise FileNotFoundError("Falha crítica: O arquivo não foi criado ou está vazio.")
        

        ContagensDatas.inserir_contagens(usuario_id, contagens)

        ContagensDatasTemporaria.excluir_contagem(usuario_id)


        return True, "<span class='mensagem-sucesso'>Sucesso ao Enviar a Contagem!</span>", ""

    except Exception as erro:
        return False, "<span class='mensagem-erro'>Erro ao Enviar a Contagem!</span>", erro
