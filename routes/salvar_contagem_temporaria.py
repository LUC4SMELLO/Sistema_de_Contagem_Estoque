from flask import Blueprint, request, flash, redirect, url_for, render_template, session, Response

from datetime import date

from scripts.processar_arquivo_parametro import lista_produtos

from backend.models.contagem import Contagem


salvar_contagem_temporaria_bp = Blueprint("contagem_temporaria", __name__)

@salvar_contagem_temporaria_bp.route("/salvar_contagem_temporaria", methods=["POST"])
def salvar_contagem_temporaria():

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")

    usuario_id = session.get("usuario_id")

    
    codigo_produto = request.form.get("produto_id")
    quantidade = request.form.get("quantidade")

    if not quantidade:
        quantidade = 0

    nova_contagem = Contagem(
        data_atual_formatada,
        usuario_id,
        codigo_produto,
        quantidade
        )
        
    nova_contagem.inserir_contagem()

    return Response(status=204)