from flask import Blueprint, flash, request, session, render_template, redirect, url_for

from models.trocas import Trocas

from constants.lista_produtos import bebidas

from scripts.salvar_trocas import salvar_troca


trocas_bp = Blueprint("trocas", __name__)

@trocas_bp.route("/trocas", methods=["GET"])
def trocas():
    return render_template("trocas.html")


@trocas_bp.route("/adicionar", methods=["GET", "POST"])
def adicionar():
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


@trocas_bp.route("/excluir", methods=["GET", "POST"])
def excluir():
    
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


@trocas_bp.route("/visualizar", methods=["GET", "POST"])
def visualizar():

    if request.method == "POST":

        codigo_produto = request.form.get("concluir")

        Trocas.concluir_troca(codigo_produto)

        dados_trocas = Trocas.buscar_trocas()
        return redirect(url_for("trocas.visualizar"))

    dados_trocas = Trocas.buscar_trocas()
    return render_template("visualizar_trocas.html", dados_trocas=dados_trocas)
