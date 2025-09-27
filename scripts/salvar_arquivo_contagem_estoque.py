import pandas as pd

def salvar_arquivo_contagem_estoque(contagens):

    lista_linhas = [{"codigo_produto": chave, "quantidade": valor} for chave, valor in contagens.items()]

    contagem = pd.DataFrame(lista_linhas)

    contagem.to_csv(f"arquivos/contagem_estoque.csv", index=False)
