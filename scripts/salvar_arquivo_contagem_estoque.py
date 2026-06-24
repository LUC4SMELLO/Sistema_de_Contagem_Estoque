from typing import List, Tuple

import pandas as pd

from constants.paths import EXPORT_CONTAGEM_ESTOQUE


def salvar_arquivo_contagem_estoque(contagens: List[Tuple]) -> None:
    """
    Salva um arquivo .csv com a contagem feita pelo usuário.

    Parameters
    ----------
        contagens
            Uma lista de tuplas com as contagens.

    Returns
    ----------
        None
    """

    contagem_estoque = pd.DataFrame(contagens)

    contagem_estoque.to_csv(EXPORT_CONTAGEM_ESTOQUE / "contagem_estoque.csv", index=False)
