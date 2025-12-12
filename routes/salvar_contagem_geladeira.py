# backend_geladeira.py
from flask import Blueprint, render_template, request, session, jsonify
from datetime import date
import csv
import os
import pandas as pd


salvar_contagem_geladeiras_bp = Blueprint("salvar_contagem_geladeiras", __name__)



@salvar_contagem_geladeiras_bp.route("/salvar_contagem_geladeiras", methods=["POST"])
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


    nome_arquivo = f"contagem_geladeiras_{data_formatada}_{usuario_id}.csv"


    contagem_estoque = pd.DataFrame(contagens)

    contagem_estoque.to_csv(f"arquivos/contagem_geladeiras.csv", index=False)

    return jsonify({"status": "ok", "arquivo": nome_arquivo})
