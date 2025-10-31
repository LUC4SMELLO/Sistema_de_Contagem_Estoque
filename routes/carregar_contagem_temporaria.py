from flask import Blueprint, request, flash, redirect, url_for, render_template, session, jsonify

from datetime import date

from scripts.processar_arquivo_parametro import lista_produtos

from backend.models.contagem_temporaria import ContagemTemporaria

carregar_contagem_temporaria_bp = Blueprint("carregar_contagem_temporaria", __name__)

@carregar_contagem_temporaria_bp.route("/carregar_contagem_temporaria")
def carregar_contagem_temporaria():

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")

    usuario_id = session.get("usuario_id")

    if not usuario_id or not data_atual_formatada:
        return jsonify([])

    dados = ContagemTemporaria.carregar_contagem(usuario_id, data_atual_formatada)

    return jsonify(dados)