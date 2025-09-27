import pandas as pd

arquivo_parametros = pd.read_csv(
    "arquivos/PRODUTOS.CSV",
    header=0,
    delimiter=";",
    encoding="ISO-8859-1",
    index_col=False
    )
arquivo_parametros.drop(columns=['Complemento', 'UN', 'Grupo',
       'Categoria', 'Marca', 'Custo G', 'Custo C', 'Custo UE',
       'Data UE', 'Fat.GN', 'Peso Bruto', 'Peso Líquido', 'Vol Embalagem',
       'Qtda por Pallet', 'Qtda por Lastro', 'Grp Carg', 'Seq Grp Carg',
       'Cx/Emb', 'Pos Item', 'Rest Gaiola', 'Qnt Emb', 'Qnt Chapatex',
       'Situação', 'Descicao Fiscal'], inplace=True)

arquivo_parametros["Codigo"] = arquivo_parametros["Codigo"].astype(str)
arquivo_parametros["Cod. CIA"] = arquivo_parametros["Cod. CIA"].astype(str)
arquivo_parametros["Descrição"] = arquivo_parametros["Descrição"].astype(str)

arquivo_parametros["Saldo Atual"] = pd.to_numeric(arquivo_parametros["Saldo Atual"], errors="coerce")
arquivo_parametros["Saldo Atual"] = arquivo_parametros["Saldo Atual"].fillna(0).astype(int)

arquivo_parametros["Cod. CIA"] = arquivo_parametros["Cod. CIA"].str.lstrip("0")

arquivo_parametros.rename(columns={"Descrição": "Descricao"}, inplace=True)