from flask import Blueprint, render_template


layout_estoque = [
    {
        "rua": "1",
        "bloco": "1",
        "coluna": "A",
        "nivel": "1",
        "data": "19/06/2026"
    },
    {
        "rua": "1",
        "bloco": "1",
        "coluna": "B",
        "nivel": "1",
        "data": "19/06/2026"
    },
    {
        "rua": "1",
        "bloco": "2",
        "coluna": "A",
        "nivel": "2",
        "data": "19/06/2026"
    },
    {
        "rua": "2",
        "bloco": "1",
        "coluna": "C",
        "nivel": "1",
        "data": "19/06/2026"
    },
    {
        "rua": "2",
        "bloco": "3",
        "coluna": "A",
        "nivel": "3",
        "data": "19/06/2026"
    }
]

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
    return render_template("contagem_datas.html", layout_estoque=layout_estoque, lista_produtos=lista_produtos)