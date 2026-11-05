from flask import Blueprint, request, render_template, flash

from models.trocas import Trocas

from constants.lista_produtos import bebidas

excluir_troca_bp = Blueprint("excluir_troca", __name__)


@excluir_troca_bp.route("/excluir_troca", methods=["GET", "POST"])
def excluir_troca():

    if request.method == "POST":
        acao = request.form.get("acao")
        id = request.form.get("id")

        produto = request.form.get("produto")
        quantidade = request.form.get("quantidade")

        if acao == "buscar":

            if not id:
                flash("Preencha o campo id.", "erro")
                return render_template("excluir_troca.html")

            codigo_produto, quantidade = Trocas.buscar_troca(id)
            if not codigo_produto or not quantidade:
                flash("Troca não encontrada.", "erro")
                return render_template("excluir_troca.html", id="", produto="", quantidade="")

            bebidas_indexada = {bebida["codigo"]: bebida["nome"] for bebida in bebidas}
            produto = bebidas_indexada.get(codigo_produto)

            return render_template("excluir_troca.html", id=id, produto=produto, quantidade=quantidade)

        if acao == "confirmar":

            if not id or not produto or not quantidade:
                flash("Busque a troca primeiro.", "aviso")
                return render_template("excluir_troca.html")

            Trocas.excluir_troca(id)

            mensagem = "<span class='mensagem-sucesso'>Sucesso ao Excluir a Troca!</span>"
            erro = ""
            
            return render_template("salvar_contagem.html", mensagem=mensagem, erro=erro)

    return render_template("excluir_troca.html")
