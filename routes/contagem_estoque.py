from flask import Blueprint, render_template

produtos = [
    {"id": "8533", "nome": "Coca Cola Lata 350ml"},
    {"id": "9334", "nome": "Coca Cola Zero Lata 350ml"},
    {"id": "56600", "nome": "Coca Cola 2L"}
]

contagem_estoque_bp = Blueprint("contagem_estoque", __name__)

@contagem_estoque_bp.route("/contagem_estoque", methods=["GET"])
def contagem_estoque():
    return render_template("contagem_estoque.html", produtos=produtos)