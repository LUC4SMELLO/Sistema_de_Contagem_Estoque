from flask import Blueprint, render_template, request, session

from constants.lista_produtos import bebidas
from scripts.salvar_arquivo_contagem_estoque import salvar_arquivo_contagem_estoque

from models.contagem_temporaria import ContagemTemporaria

from models.contagens import Contagens

from datetime import date


salvar_contagem_bp = Blueprint("salvar_contagem", __name__)

@salvar_contagem_bp.route("/salvar_contagem", methods=["POST"])
def salvar_contagem():

    usuario_id = session.get("usuario_id")
    

    contagens = []

    for produto in bebidas:
        campo = f"produto_{produto['codigo']}"
        quantidade = request.form.get(campo)

        if not quantidade:
            quantidade = 0

        contagens.append({
            "codigo": produto["codigo"],
            "nome": produto["nome"],
            "quantidade": int(quantidade)
        })

        
    salvar_arquivo_contagem_estoque(contagens, usuario_id)


    return render_template("salvar_contagem.html")
