from flask import Blueprint, request, render_template

contagem_geladeira_bp = Blueprint("contagem_geladeira", __name__)

@contagem_geladeira_bp.route("/contagem_geladeira", methods=["GET"])
def contagem_geladeira():

    return render_template("contagem_geladeira.html")