from flask import Blueprint, render_template

from scripts.processar_arquivo_parametro import lista_produtos

contagem_estoque_bp = Blueprint("contagem_estoque", __name__)

@contagem_estoque_bp.route("/contagem_estoque", methods=["GET"])
def contagem_estoque():
    return render_template("contagem_estoque.html", produtos=lista_produtos)