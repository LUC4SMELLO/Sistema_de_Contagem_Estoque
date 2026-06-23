from flask import Blueprint, request, session, Response

from datetime import date

from models.contagens_datas_temporaria import ContagensDatasTemporaria


salvar_contagem_datas_temporaria_bp = Blueprint("salvar_contagem_datas_temporaria", __name__)

@salvar_contagem_datas_temporaria_bp.route('/salvar_contagem_datas_temporaria', methods=['POST'])
def salvar_contagem_datas_temporaria():

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%Y-%m-%d")

    usuario_id = session.get("usuario_id")

    id = request.form.get('id')
    rua = request.form.get('rua')
    bloco = request.form.get('bloco')
    coluna = request.form.get('coluna')
    nivel = request.form.get('nivel')

    chave = f"R{rua}-B{bloco}-C{coluna}-N{nivel}"

    codigo_produto = request.form.get('codigo_produto')
    data_fabricacao = request.form.get('data_fabricacao')
    data_validade = request.form.get('data_validade')


    ContagensDatasTemporaria.inserir_contagem(
        data_atual_formatada,
        usuario_id,
        rua,
        bloco,
        coluna,
        nivel,
        chave,
        codigo_produto,
        data_fabricacao,
        data_validade
    )


    return Response(status=204)
