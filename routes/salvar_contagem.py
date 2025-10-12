from flask import Blueprint, render_template, request

from scripts.processar_arquivo_parametro import lista_produtos
from scripts.salvar_arquivo_contagem_estoque import salvar_arquivo_contagem_estoque

salvar_contagem_bp = Blueprint("salvar_contagem", __name__)

@salvar_contagem_bp.route("/salvar_contagem", methods=["POST"])
def salvar_contagem():

    contagens = []

    for produto in lista_produtos:
        campo = f"produto_{produto['id']}"
        quantidade = request.form.get(campo)

        if not quantidade:
            quantidade = 0

        contagens.append({
            "codigo": produto["id"],
            "nome": produto["nome"],
            "quantidade": int(quantidade)
        })

    salvar_arquivo_contagem_estoque(contagens)

    # SALVAR NO BANCO DE DADOS

    return render_template("salvar_contagem.html")
