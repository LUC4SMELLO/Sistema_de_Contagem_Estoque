from flask import Blueprint, request, session, jsonify
from datetime import date
import pandas as pd

from models.contagem_temporaria import ContagemTemporaria

from scripts.salvar_arquivo_contagem_geladeiras import salvar_arquivo_contagem_geladeiras


salvar_contagem_geladeiras_bp = Blueprint("salvar_contagem_geladeiras", __name__)

@salvar_contagem_geladeiras_bp.route("/salvar_contagem_geladeiras", methods=["GET", "POST"])
def salvar_contagem_geladeiras():


    data_atual = date.today()
    data_formatada = data_atual.strftime("%d/%m/%Y")

    usuario_id = session.get("usuario_id", "desconhecido")

    dados = request.get_json()
    itens = dados.get("itens", [])

    if not itens:
        return jsonify({"status": "erro", "mensagem": "Nenhuma geladeira enviada."})

    
    contagens = []
    for codigo in itens:
        contagens.append({
            "codigo": codigo,
            "quantidade": 1
        })

    salvar_arquivo_contagem_geladeiras(contagens)

    ContagemTemporaria.excluir_contagem(usuario_id)


    return jsonify({"status": "ok"})
