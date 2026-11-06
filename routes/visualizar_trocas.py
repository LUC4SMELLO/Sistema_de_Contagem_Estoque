from flask import Blueprint, request, render_template, redirect, url_for

from models.trocas import Trocas


visualizar_trocas_bp = Blueprint("visualizar_trocas", __name__)

@visualizar_trocas_bp.route("/visualizar_trocas", methods=["GET", "POST"])
def visualizar_trocas():

    if request.method == "POST":

        codigo_produto = request.form.get("concluir")

        Trocas.concluir_troca(codigo_produto)

        dados_trocas = Trocas.buscar_trocas()
        return redirect(url_for("visualizar_trocas.visualizar_trocas"))

    dados_trocas = Trocas.buscar_trocas()
    return render_template("visualizar_trocas.html", dados_trocas=dados_trocas)
