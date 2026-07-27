from flask import Blueprint, render_template


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada")
def relatorio_entrada():
    return render_template("relatorio_entrada.html")
