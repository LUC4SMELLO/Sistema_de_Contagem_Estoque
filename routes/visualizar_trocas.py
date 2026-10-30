from flask import Blueprint, render_template


visualizar_trocas_bp = Blueprint("visualizar_trocas", __name__)

@visualizar_trocas_bp.route("/visualizar_trocas", methods=["GET", "POST"])
def visualizar_trocas():

    return render_template("visualizar_trocas.html")
