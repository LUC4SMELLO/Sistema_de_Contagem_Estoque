from flask import Blueprint, session, render_template, request

from constants.lista_produtos import bebidas

from scripts.salvar_trocas import salvar_troca


adicionar_troca_bp = Blueprint("adicionar_troca", __name__)

@adicionar_troca_bp.route("/adicionar_troca", methods=["GET", "POST"])
def adicionar_troca():

    if request.method == "POST":

        usuario_id = session.get("usuario_id")

        codigo_produto = request.form.get("produto")
        quantidade = request.form.get("quantidade")


        troca = {
            "codigo_produto": codigo_produto,
            "quantidade": quantidade
        }


        resultado, mensagem, erro = salvar_troca(usuario_id, troca)

        return render_template("salvar_contagem.html", mensagem=mensagem, erro=erro)

    return render_template("adicionar_troca.html", lista_produtos=bebidas)
