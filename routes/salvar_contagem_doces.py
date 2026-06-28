from flask import Blueprint, render_template, request, session

from models.contagens import Contagens
from models.contagem_temporaria import ContagemTemporaria

from datetime import date

from constants.lista_produtos import doces
from scripts.salvar_arquivo_contagem_doces import salvar_arquivo_contagem_doces


salvar_contagem_doces_bp = Blueprint("salvar_contagem_doces", __name__)

@salvar_contagem_doces_bp.route("/salvar_contagem_doces", methods=["POST"])
def salvar_contagem_doces():

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")

    usuario_id = session.get("usuario_id")
    

    contagens = []

    for produto in doces:
        campo = f"produto_{produto['codigo']}"
        quantidade = request.form.get(campo)

        if not quantidade:
            quantidade = 0

        contagens.append({
            "codigo": produto["codigo"],
            "nome": produto["nome"],
            "quantidade": int(quantidade)
        })

        
    resultado, mensagem, erro = salvar_arquivo_contagem_doces(contagens, usuario_id)

    return render_template("salvar_contagem.html", mensagem=mensagem, erro=erro)
