from flask import Blueprint, session, jsonify

from models.relatorios_entradas_temporarios import RelatoriosEntradasTemporarios


carregar_relatorio_entrada_temporario_bp = Blueprint("carregar_relatorio_entrada_temporario", __name__)

@carregar_relatorio_entrada_temporario_bp.route("/carregar_relatorio_entrada_temporario")
def carregar_relatorio_entrada_temporario():

    usuario_id = session.get("usuario_id")

    dados = RelatoriosEntradasTemporarios.buscar_relatorio_temporarios(usuario_id)

    return jsonify(dados)