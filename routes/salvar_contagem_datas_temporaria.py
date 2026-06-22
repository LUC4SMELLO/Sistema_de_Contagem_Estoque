from flask import Blueprint, request, Response


salvar_contagem_datas_temporaria_bp = Blueprint("salvar_contagem_datas_temporaria", __name__)

@salvar_contagem_datas_temporaria_bp.route('/salvar_contagem_datas_temporaria', methods=['POST'])
def salvar_contagem_datas_temporaria():

    id = request.form.get('id')
    rua = request.form.get('rua')
    bloco = request.form.get('bloco')
    coluna = request.form.get('coluna')
    nivel = request.form.get('nivel')

    codigo_produto = request.form.get('codigo_produto')
    data_fabricacao = request.form.get('data_fabricacao')
    data_validade = request.form.get('data_validade')

    print(
        id,
        rua,
        bloco,
        coluna,
        nivel,
        codigo_produto,
        data_fabricacao,
        data_validade
    )

    # Salvar no banco


    return Response(status=204)
