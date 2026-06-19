from flask import Blueprint, request
salvar_contagem_datas_bp = Blueprint("salvar_contagem_datas", __name__)

@salvar_contagem_datas_bp.route('/salvar_contagem_datas', methods=['POST'])
def salvar_contagem_datas():
    # Captura as listas de cada coluna enviada pelo formulário
    ruas = request.form.getlist('rua[]')
    blocos = request.form.getlist('bloco[]')
    colunas = request.form.getlist('coluna[]')
    niveis = request.form.getlist('nivel[]')
    produtos = request.form.getlist('produto[]')
    datas = request.form.getlist('data[]')

    # Processa os dados linha por linha usando o zip do Python
    for r, b, c, n, prod, dt in zip(ruas, blocos, colunas, niveis, produtos, datas):
        # Ignora linhas onde o produto ou a data não foram preenchidos
        if not prod or not dt:
            continue
            
        print(f"Salvando: Rua {r}, Bloco {b}, Coluna {c}, Nível {n} -> Produto: {prod} em {dt}")
        # Aqui você insere a lógica para salvar no seu Banco de Dados

    return "Contagem salva com sucesso!"
