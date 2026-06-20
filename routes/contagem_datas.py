from flask import Blueprint, render_template

from constantes.layout_estoque import enderecos

lista_produtos = [
    {"nome": "Coca Cola 2L"},
    {"nome": "Coca 350ml"},
    {"nome": "Coca Zero 2L"},
    {"nome": "Coca Cola Sem Açúcar 350ml"},
    {"nome": "Coca Cola Garrafa 600ml"},
    {"nome": "Coca Cola Sem Açúcar 600ml"},
    {"nome": "Coca Cola Café 220ml"},
    {"nome": "Coca Cola Cherry 355ml"},
    {"nome": "Fanta Laranja 2L"},
    {"nome": "Sprite 2L"}
]


contagem_datas_bp = Blueprint("contagem_datas", __name__)

@contagem_datas_bp.route("/contagem_datas", methods=["GET", "POST"])
def contagem_datas():
    return render_template("contagem_datas.html", layout_estoque=enderecos, lista_produtos=lista_produtos)