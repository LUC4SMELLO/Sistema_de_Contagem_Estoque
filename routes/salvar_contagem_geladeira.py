# backend_geladeira.py
from flask import Blueprint, render_template, request, session, jsonify
from datetime import date
import csv
import os

contagem_geladeiras_bp = Blueprint("contagem_geladeiras", __name__)

PASTA_SAIDA = "arquivos"
os.makedirs(PASTA_SAIDA, exist_ok=True)

@contagem_geladeiras_bp.route("/salvar_geladeiras", methods=["POST"])
def salvar_geladeiras():
    data_atual = date.today()
    data_formatada = data_atual.strftime("%d-%m-%Y")

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


    nome_arquivo = f"contagem_geladeiras_{data_formatada}_{usuario_id}.csv"
    caminho_arquivo = os.path.join(PASTA_SAIDA, nome_arquivo)

    with open(caminho_arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["codigo", "quantidade"])
        for item in contagens:
            writer.writerow([item["codigo"], item["quantidade"]])


    return jsonify({"status": "ok", "arquivo": nome_arquivo})
