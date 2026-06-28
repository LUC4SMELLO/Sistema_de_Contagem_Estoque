from flask import Blueprint, request, session, jsonify, render_template

from scripts.salvar_arquivo_contagem_geladeiras import salvar_arquivo_contagem_geladeiras


salvar_contagem_geladeiras_bp = Blueprint("salvar_contagem_geladeiras", __name__)

@salvar_contagem_geladeiras_bp.route("/salvar_contagem_geladeiras", methods=["GET", "POST"])
def salvar_contagem_geladeiras():

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

    resultado, mensagem, erro = salvar_arquivo_contagem_geladeiras(contagens, usuario_id)


    return jsonify({"status": "ok"})
