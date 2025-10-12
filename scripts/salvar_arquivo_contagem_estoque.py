import pandas as pd

def salvar_arquivo_contagem_estoque(contagens):

    contagem_estoque = pd.DataFrame(contagens)

    contagem_estoque.to_csv(f"arquivos/contagem_estoque.csv", index=False)
