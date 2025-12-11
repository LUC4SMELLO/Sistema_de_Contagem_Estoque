from flask import Blueprint, render_template, request, session

from backend.models.contagens import Contagens
from backend.models.contagem_temporaria import ContagemTemporaria

from datetime import date

from scripts.processar_arquivo_parametro_doces import lista_doces
from scripts.salvar_arquivo_contagem_doces import salvar_arquivo_contagem_doces

salvar_contagem_doces_bp = Blueprint("salvar_contagem_doces", __name__)

@salvar_contagem_doces_bp.route("/salvar_contagem_doces", methods=["POST"])
def salvar_contagem_doces():

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")

    usuario_id = session.get("usuario_id")
    

    contagens = []

    for produto in lista_doces:
        campo = f"produto_{produto['id']}"
        quantidade = request.form.get(campo)

        if not quantidade:
            quantidade = 0

        contagens.append({
            "codigo": produto["id"],
            "nome": produto["nome"],
            "quantidade": int(quantidade)
        })

        
    salvar_arquivo_contagem_doces(contagens)

    Contagens.inserir_contagens(usuario_id, contagens)
    
    ContagemTemporaria.excluir_contagem(usuario_id, data_atual_formatada)


    return render_template("salvar_contagem.html")