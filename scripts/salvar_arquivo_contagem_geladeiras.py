from typing import List, Tuple

import pandas as pd

from constants.paths import EXPORT_CONTAGEM_GELADEIRAS


def salvar_arquivo_contagem_geladeiras(contagens: List[Tuple]) -> None:
    """
    Salva um arquivo .csv com a contagem de geladeiras feita pelo usuário.

    Parameters
    ----------
        contagens
            Uma lista de tuplas com as contagens.

    Returns
    ----------
        None
    """

    contagem_geladeiras = pd.DataFrame(contagens)

    contagem_geladeiras.to_csv(EXPORT_CONTAGEM_GELADEIRAS / "contagem_geladeiras.csv", index=False)
