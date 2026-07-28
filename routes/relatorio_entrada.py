from flask import Blueprint, render_template

from teste_xml import ler_arquivo_xml
from constants.paths import IMPORTS

CAMINHO_XML = IMPORTS / "50_13633613_Luis_FDB7977_Betim.xml"


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada")
def relatorio_entrada():

    dados = ler_arquivo_xml(CAMINHO_XML)

    return render_template("relatorio_entrada.html", nota=dados)
