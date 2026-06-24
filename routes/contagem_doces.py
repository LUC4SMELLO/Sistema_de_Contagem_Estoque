from flask import Blueprint, render_template

from constants.lista_produtos import doces


contagem_doces_bp = Blueprint("contagem_doces", __name__)

@contagem_doces_bp.route("/contagem_doces", methods=["GET"])
def contagem_doces():
    return render_template("contagem_doces.html", produtos=doces)
