
estrutura = {
    1: {  # Rua
        1: {  # Bloco
            "A": 3, # Coluna e Quantidade de Níveis
            "B": 3,
            "C": 5
        },
        2: {
            "A": 5,
            "B": 5,
            "C": 3
        }
    }
}

enderecos = []
for rua, blocos in estrutura.items():

    for bloco, colunas in blocos.items():

        for coluna, qtd_niveis in colunas.items():

            for nivel in range(1, qtd_niveis + 1):

                enderecos.append({
                    "rua": rua,
                    "bloco": bloco,
                    "coluna": coluna,
                    "nivel": nivel
                })
