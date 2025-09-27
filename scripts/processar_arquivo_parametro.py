import pandas as pd

arquivo_parametro = pd.read_csv(
    "arquivos/PRODUTOS.CSV",
    header=0,
    delimiter=";",
    encoding="ISO-8859-1",
    index_col=False
    )

arquivo_parametro.drop(columns=['Complemento', 'UN',
       'Categoria', 'Marca', 'Custo G', 'Custo C', 'Custo UE',
       'Data UE', 'Fat.GN', 'Peso Bruto', 'Peso Líquido', 'Vol Embalagem',
       'Qtda por Pallet', 'Qtda por Lastro', 'Grp Carg', 'Seq Grp Carg',
       'Cx/Emb', 'Pos Item', 'Rest Gaiola', 'Qnt Emb', 'Qnt Chapatex',
       'Situação', 'Descicao Fiscal'], inplace=True)

arquivo_parametro["Codigo"] = arquivo_parametro["Codigo"].astype(str)
arquivo_parametro["Cod. CIA"] = arquivo_parametro["Cod. CIA"].astype(str)
arquivo_parametro["Descrição"] = arquivo_parametro["Descrição"].astype(str)

arquivo_parametro["Saldo Atual"] = pd.to_numeric(arquivo_parametro["Saldo Atual"], errors="coerce")
arquivo_parametro["Saldo Atual"] = arquivo_parametro["Saldo Atual"].fillna(0).astype(int)

arquivo_parametro["Cod. CIA"] = arquivo_parametro["Cod. CIA"].str.lstrip("0")

arquivo_parametro.rename(columns={"Descrição": "Descricao"}, inplace=True)

# ESTE TRECHO EXCLUI DETERMINADOS GRUPOS DE PRODUTOS
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '099-MATERIAL                  ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '013-BALAS E GOMAS             ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '020-ALIMENTOS                 ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '019-SNACKS                    ']

# ESTE TRECHO FILTRA O GÁS CERTO
arquivo_parametro = arquivo_parametro[
    (arquivo_parametro["Grupo"] != "023-GAS CO2                   ") |
    ((arquivo_parametro["Grupo"] == "023-GAS CO2                   ") &
     (arquivo_parametro["Codigo"].isin(["120120", "120121"])))
]

arquivo_parametro.drop(columns=["Grupo"], inplace=True)


lista_produtos = [
    {"id": row["Codigo"], "nome": row["Descricao"]}
    for _, row in arquivo_parametro.iterrows()
]
