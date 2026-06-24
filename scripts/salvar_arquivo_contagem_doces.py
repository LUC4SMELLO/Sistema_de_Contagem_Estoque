from typing import List, Tuple

import pandas as pd

from constants.paths import EXPORT_CONTAGEM_ESTOQUE_DOCES


def salvar_arquivo_contagem_doces(contagens: List[Tuple]) -> None:
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

    contagem_estoque.to_csv(EXPORT_CONTAGEM_ESTOQUE_DOCES / "contagem_doces.csv", index=False)
