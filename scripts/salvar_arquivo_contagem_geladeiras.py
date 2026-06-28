import os
from typing import List, Tuple

from datetime import datetime

import pandas as pd

from constants.paths import EXPORT_CONTAGEM_GELADEIRAS

from models.contagem_temporaria import ContagemTemporaria


def salvar_arquivo_contagem_geladeiras(contagens: List[Tuple], usuario_id) -> None:
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

    try:

        data_atual = datetime.now()
        data_atual_formatada_arquivo = data_atual.strftime("%d-%m-%Y_%H-%M-%S")

        contagem_geladeiras = pd.DataFrame(contagens)

        CAMINHO_SALVAR_ARQUIVO_CSV = EXPORT_CONTAGEM_GELADEIRAS / f"contagem_geladeiras_{data_atual_formatada_arquivo}.csv"

        contagem_geladeiras.to_csv(CAMINHO_SALVAR_ARQUIVO_CSV, index=False)


        if not os.path.exists(CAMINHO_SALVAR_ARQUIVO_CSV) or os.path.getsize(CAMINHO_SALVAR_ARQUIVO_CSV) == 0:
            raise FileNotFoundError("Falha crítica: O arquivo não foi criado ou está vazio.")


        ContagemTemporaria.excluir_contagem(usuario_id)

        return True, "<span class='mensagem-sucesso'>Sucesso ao Enviar a Contagem!</span>", ""

    except Exception as erro:
        return False, "<span class='mensagem-erro'>Erro ao Enviar a Contagem!</span>", erro
