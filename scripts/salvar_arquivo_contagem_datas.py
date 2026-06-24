from typing import List, Tuple

from datetime import datetime

import pandas as pd

from constants.paths import EXPORT_CONTAGEM_DATAS


def salvar_arquivo_contagem_datas(contagens: List[Tuple]) -> None:
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

    data_atual = datetime.now()
    data_atual_formatada = data_atual.strftime("%d-%m-%Y %H:%M:%S")
    data_atual_formatada = data_atual_formatada.replace(":", "-")

    contagem_data = pd.DataFrame(contagens)

    contagem_data["data_validade"] = pd.to_datetime(contagem_data["data_validade"])
    contagem_data["data_fabricacao"] = pd.to_datetime(contagem_data["data_fabricacao"])

    contagem_data["data_validade"] = contagem_data["data_validade"].dt.strftime('%d/%m/%Y')
    contagem_data["data_fabricacao"] = contagem_data["data_fabricacao"].dt.strftime('%d/%m/%Y')


    contagem_data.to_csv(EXPORT_CONTAGEM_DATAS / f"contagem_datas_{data_atual_formatada}.csv", index=False)
