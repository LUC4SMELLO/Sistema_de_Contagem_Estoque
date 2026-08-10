import re
from datetime import datetime

from flask import Blueprint, render_template, request

from services.relatorio_entrada import buscar_relatorios_inseridos, buscar_relatorio_entrada


visualizar_relatorio_entrada_bp = Blueprint("visualizar_relatorio_entrada", __name__)

@visualizar_relatorio_entrada_bp.route("/visualizar_relatorio_entrada", methods=["GET", "POST"])
def visualizar_relatorio_entrada():

    
    cargas = buscar_relatorios_inseridos()
    carga_selecionada = None

    if request.method == "POST":

        acao = request.form.get("acao")

        if acao == "buscar":

            carga = request.form.get("carga")

            carga_selecionada, relatorio = buscar_relatorio_entrada(carga)
            

            return render_template("visualizar_relatorio_entrada.html", cargas=cargas, dados_produtos=relatorio, carga_selecionada=carga_selecionada)
        

    return render_template("visualizar_relatorio_entrada.html", cargas=cargas, dados_produtos="", carga_selecionada=carga_selecionada)
