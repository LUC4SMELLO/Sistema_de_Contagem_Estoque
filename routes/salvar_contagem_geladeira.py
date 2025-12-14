from flask import Blueprint, request, session, jsonify
from datetime import date
import pandas as pd

from backend.models.contagem_temporaria import ContagemTemporaria

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

    contagem_estoque = pd.DataFrame(contagens)

    contagem_estoque.to_csv(f"arquivos/contagem_geladeiras.csv", index=False)

    ContagemTemporaria.excluir_contagem(usuario_id, data_formatada)


    return jsonify({"status": "ok"})