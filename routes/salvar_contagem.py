from flask import Blueprint, render_template, request

from scripts.processar_arquivo_parametro import lista_produtos

salvar_contagem_bp = Blueprint("salvar_contagem", __name__)

@salvar_contagem_bp.route("/salvar_contagem", methods=["POST"])
def salvar_contagem():

    contagens = {}

    for produto in lista_produtos:
        campo = f"produto_{produto['id']}"  # EXEMPLO: "produto_1"

        quantidade = request.form.get(campo)  # PEGA O VALOR DO FORMULÁRIO

        print(quantidade)

        if quantidade:
            contagens[produto["id"]] = int(quantidade)

        else:
            contagens[produto["id"]] = int(0)
        

    print("Valores recebidos:", contagens) 
    # SALVAR NO BANCO DE DADOS

    return "Contagem recebida com sucesso!"
