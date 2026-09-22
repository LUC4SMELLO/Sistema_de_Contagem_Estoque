from flask import Blueprint, render_template

from services.contagem_datas import buscar_produtos_com_data_curta


relatorio_datas_bp = Blueprint("relatorio_datas", __name__)

@relatorio_datas_bp.route("/relatorio_datas", methods=["GET"])
def relatorio_datas():

    produtos = buscar_produtos_com_data_curta()

    return render_template("relatorio_datas.html", produtos=produtos)
