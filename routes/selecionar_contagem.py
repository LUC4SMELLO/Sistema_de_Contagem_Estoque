from flask import Blueprint, render_template

selecionar_contagem_bp = Blueprint("selecionar_contagem", __name__)

@selecionar_contagem_bp.route("/selecionar_contagem", methods=["GET"])
def selecionar_contagem():

    return render_template("selecionar_contagem.html")