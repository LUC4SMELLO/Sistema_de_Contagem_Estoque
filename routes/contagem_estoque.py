from flask import Blueprint, render_template

produtos = [
    {"id": "8533", "nome": "Coca Cola Lata 350ml"},
    {"id": "9334", "nome": "Coca Cola Zero Lata 350ml"},
    {"id": "56600", "nome": "Coca Cola 2L"},
    {"id": "55286", "nome": "Fanta Uva Lata 350ml"},
    {"id": "55935", "nome": "Coca Cola 600ml"},
    {"id": "8463", "nome": "Energético Monster Energy 473ml"},
    {"id": "139441", "nome": "Whiskey Red Label 750ml"},
    {"id": "7331", "nome": "Água Sem Gás 500ml"}
]

contagem_estoque_bp = Blueprint("contagem_estoque", __name__)

@contagem_estoque_bp.route("/contagem_estoque", methods=["GET"])
def contagem_estoque():
    return render_template("contagem_estoque.html", produtos=produtos)