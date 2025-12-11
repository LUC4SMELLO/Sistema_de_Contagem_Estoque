from flask import Blueprint, render_template

from scripts.processar_arquivo_parametro_doces import lista_doces

contagem_doces_bp = Blueprint("contagem_doces", __name__)

@contagem_doces_bp.route("/contagem_doces", methods=["GET"])
def contagem_doces():
    return render_template("contagem_doces.html", produtos=lista_doces)