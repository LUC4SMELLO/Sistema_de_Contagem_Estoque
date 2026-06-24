from flask import Blueprint, request, session, render_template

from models.contagens_datas import ContagensDatas

from models.contagens_datas_temporaria import ContagensDatasTemporaria

from constants.lista_produtos import bebidas

from scripts.salvar_arquivo_contagem_datas import salvar_arquivo_contagem_datas


salvar_contagem_datas_bp = Blueprint("salvar_contagem_datas", __name__)

@salvar_contagem_datas_bp.route('/salvar_contagem_datas', methods=['POST'])
def salvar_contagem_datas():

    usuario_id = session.get("usuario_id")

    # Captura as listas de cada coluna enviada pelo formulário
    id = request.form.getlist('id[]')
    ruas = request.form.getlist('rua[]')
    blocos = request.form.getlist('bloco[]')
    colunas = request.form.getlist('coluna[]')
    niveis = request.form.getlist('nivel[]')
    produtos = request.form.getlist('produto[]')
    data_fabricacao = request.form.getlist('data_fabricacao[]')
    data_validade = request.form.getlist('data_validade[]')


    produtos_dict = {
        str(produto["codigo"]): produto["nome"]
        for produto in bebidas
    }


    contagens = []
    # Processa os dados linha por linha usando o zip do Python
    for id, rua, bloco, coluna, nivel, codigo, data_fabricacao, data_validade, in zip(id, ruas, blocos, colunas, niveis, produtos, data_fabricacao, data_validade):

        contagens.append({
            "id": id,
            "rua": rua,
            "bloco": bloco,
            "coluna": coluna,
            "nivel": nivel,
            "codigo_produto": codigo,
            "nome": produtos_dict.get(codigo),
            "data_fabricacao": data_fabricacao,
            "data_validade": data_validade
        })

    salvar_arquivo_contagem_datas(contagens)
            
    ContagensDatas.inserir_contagens(usuario_id, contagens)

    ContagensDatasTemporaria.excluir_contagem(usuario_id)

    return render_template("salvar_contagem.html")

