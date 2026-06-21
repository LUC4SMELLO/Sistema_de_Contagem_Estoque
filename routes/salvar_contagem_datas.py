from flask import Blueprint, request, session, render_template

from models.contagens_datas import ContagensDatas

from constantes.lista_produtos import bebidas

from scripts.salvar_arquivo_contagem_datas import salvar_arquivo_contagem_datas


salvar_contagem_datas_bp = Blueprint("salvar_contagem_datas", __name__)

@salvar_contagem_datas_bp.route('/salvar_contagem_datas', methods=['POST'])
def salvar_contagem_datas():

    usuario_id = session.get("usuario_id")

    contagens = []

    # Captura as listas de cada coluna enviada pelo formulário
    ruas = request.form.getlist('rua[]')
    blocos = request.form.getlist('bloco[]')
    colunas = request.form.getlist('coluna[]')
    niveis = request.form.getlist('nivel[]')
    produtos = request.form.getlist('produto[]')
    datas = request.form.getlist('data[]')


    produtos_dict = {
        str(produto["codigo"]): produto["nome"]
        for produto in bebidas
    }

    # Processa os dados linha por linha usando o zip do Python
    for r, b, c, n, prod, dt in zip(ruas, blocos, colunas, niveis, produtos, datas):

        contagens.append({
            "rua": r,
            "bloco": b,
            "coluna": c,
            "nivel": n,
            "codigo_produto": prod,
            "nome": produtos_dict.get(prod),
            "data_contada": dt
        })

    salvar_arquivo_contagem_datas(contagens)
            
    ContagensDatas.inserir_contagens(usuario_id, contagens)

    return render_template("salvar_contagem.html")
