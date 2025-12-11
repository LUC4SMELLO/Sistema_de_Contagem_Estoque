import pandas as pd

arquivo_parametro = pd.read_csv(
    "arquivos/PRODUTOS DOCES.CSV",
    header=0,
    delimiter=";",
    encoding="ISO-8859-1",
    index_col=False
    )

arquivo_parametro.rename(columns={
    "Descriï¿½ï¿½o": "Descricao",
    "Situaï¿½ï¿½o": "Situação",
    "Peso Lï¿½quido": "Peso Líquido",
    }, inplace=True
)

arquivo_parametro.drop(columns=['Complemento', 'UN',
       'Categoria', 'Marca', 'Custo G', 'Custo C', 'Custo UE',
       'Data UE', 'Fat.GN', 'Peso Bruto', 'Peso Líquido', 'Vol Embalagem',
       'Qtda por Pallet', 'Qtda por Lastro', 'Grp Carg', 'Seq Grp Carg',
       'Cx/Emb', 'Pos Item', 'Rest Gaiola', 'Qnt Emb', 'Qnt Chapatex',
       'Situação', 'Descicao Fiscal'], inplace=True)

arquivo_parametro["Codigo"] = arquivo_parametro["Codigo"].astype(str)
arquivo_parametro["Cod. CIA"] = arquivo_parametro["Cod. CIA"].astype(str)
arquivo_parametro['Descricao'] = arquivo_parametro['Descricao'].astype(str)

arquivo_parametro["Saldo Atual"] = pd.to_numeric(arquivo_parametro["Saldo Atual"], errors="coerce")
arquivo_parametro["Saldo Atual"] = arquivo_parametro["Saldo Atual"].fillna(0).astype(int)

arquivo_parametro["Cod. CIA"] = arquivo_parametro["Cod. CIA"].str.lstrip("0")



# ESTE TRECHO EXCLUI DETERMINADOS GRUPOS DE PRODUTOS
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '099-MATERIAL                  ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '023-GAS CO2                   ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '009-SOJA                      ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '004-CHAS                      ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '014-MIXED DRINKS              ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '002-CERVEJA                   ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '007-ISOTONICO                 ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '001-REFRIG                    ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '008-SUCOS                     ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '012-SPIRITS                   ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '005-ENERGETICO                ']
arquivo_parametro = arquivo_parametro[arquivo_parametro["Grupo"] != '003-AGUA                      ']

arquivo_parametro.drop(columns=["Grupo"], inplace=True)


lista_doces = [
    {"id": row["Codigo"], "nome": row["Descricao"]}
    for _, row in arquivo_parametro.iterrows()
]
