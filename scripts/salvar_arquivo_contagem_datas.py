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

    contagem_data["data_validade"] = pd.to_datetime(contagem_data["data_validade"])
    contagem_data["data_fabricacao"] = pd.to_datetime(contagem_data["data_fabricacao"])

    contagem_data["data_validade"] = contagem_data["data_validade"].dt.strftime('%d/%m/%Y')
    contagem_data["data_fabricacao"] = contagem_data["data_fabricacao"].dt.strftime('%d/%m/%Y')


    contagem_data.to_csv(f"arquivos/contagem_datas.csv", index=False)
