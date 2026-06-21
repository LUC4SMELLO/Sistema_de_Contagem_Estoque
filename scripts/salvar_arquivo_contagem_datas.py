from typing import List, Tuple

import pandas as pd


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

    contagem_data = pd.DataFrame(contagens)

    contagem_data["data_contada"] = pd.to_datetime(contagem_data["data_contada"])
    contagem_data["data_contada"] = contagem_data["data_contada"].dt.strftime('%d/%m/%Y')


    contagem_data.to_csv(f"arquivos/contagem_datas.csv", index=False)
