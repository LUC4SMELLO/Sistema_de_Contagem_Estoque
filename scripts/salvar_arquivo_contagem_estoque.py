from typing import List, Tuple

import pandas as pd


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

    contagem_estoque.to_csv(f"arquivos/contagem_estoque.csv", index=False)
