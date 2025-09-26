import pandas as pd

arquivo_parametros = pd.read_csv("arquivos/PRODUTOS.CSV", delimiter=";", header=0, encoding="iso-8859-1")

print(arquivo_parametros)
