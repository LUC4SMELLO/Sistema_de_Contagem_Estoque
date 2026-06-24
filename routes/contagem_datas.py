from flask import Blueprint, render_template, session

from services.contagem_datas import selecionar_contagem_datas_para_carregar

from constants.layout_estoque import enderecos
from constants.lista_produtos import bebidas


contagem_datas_bp = Blueprint("contagem_datas", __name__)

@contagem_datas_bp.route("/contagem_datas", methods=["GET", "POST"])
def contagem_datas():

    usuario_id = session.get("usuario_id")

    contagem_a_carregar = selecionar_contagem_datas_para_carregar(usuario_id)

    return render_template(
        "contagem_datas.html",
        layout_estoque=enderecos,
        contagem_anterior=contagem_a_carregar,
        lista_produtos=bebidas
        )
