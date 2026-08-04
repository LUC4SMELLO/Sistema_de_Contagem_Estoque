from flask import Blueprint, request, jsonify, session, Response

from models.relatorios_entradas_temporarios import RelatoriosEntradasTemporarios


salvar_relatorio_entrada_temporario_bp = Blueprint("salvar_relatorio_entrada_temporario", __name__)

@salvar_relatorio_entrada_temporario_bp.route('/salvar_relatorio_entrada_temporario', methods=['POST'])
def salvar_relatorio_entrada_temporario():
    try:
        dados_relatorio = {
            "numero_carga": request.form.get("numero_carga"),
            "nota_fiscal": request.form.get("nota_fiscal"),
            "item": request.form.get("item"),
            "chave": request.form.get("chave"),
            "codigo_produto": request.form.get("codigo_produto"),
            "descricao": request.form.get("descricao"),
            "fabricacao": request.form.get("fabricacao"),
            "vencimento": request.form.get("vencimento"),
            "fefo": int(request.form.get("fefo", 0)),
            "pallet_danificado": int(request.form.get("pallet_danificado", 0)),
            "vazamento": int(request.form.get("vazamento", 0)),
            "observacao": request.form.get("observacao")
        }
        
        usuario_id = session.get("usuario_id")

        RelatoriosEntradasTemporarios.inserir_relatorio_temporario(usuario_id, dados_relatorio)
        
        return Response(status=204)

    except Exception:
        return Response(status=500)
