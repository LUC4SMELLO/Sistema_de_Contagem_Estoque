from flask import Blueprint, render_template, request

from scripts.ler_arquivo_xml import ler_varios_arquivos_xml
from constants.paths import IMPORTS


cargas = {
    1: IMPORTS / "1_97190_André_FHW5858_Itabirito.xml",
    2: IMPORTS / "1_13633613_André_FHW5858_Itabirito.xml",
}


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada", methods=["GET", "POST"])
def relatorio_entrada():

    dados = None
    carga_selecionada = None

    if request.method == "POST":
        carga_selecionada = request.form["carga"]

        dados = ler_varios_arquivos_xml(carga_selecionada)

    return render_template("relatorio_entrada.html", cargas=cargas, notas=dados, carga_selecionada=carga_selecionada)
