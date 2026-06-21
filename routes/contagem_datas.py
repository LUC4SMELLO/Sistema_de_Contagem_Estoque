from flask import Blueprint, render_template

from models.contagens_datas import ContagensDatas

from constantes.layout_estoque import enderecos
from constantes.lista_produtos import bebidas


contagem_datas_bp = Blueprint("contagem_datas", __name__)

@contagem_datas_bp.route("/contagem_datas", methods=["GET", "POST"])
def contagem_datas():

    contagem_anterior = ContagensDatas.buscar_ultima_contagem()

    return render_template(
        "contagem_datas.html",
        layout_estoque=enderecos,
        contagem_anterior=contagem_anterior,
        lista_produtos=bebidas
        )
