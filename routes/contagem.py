from flask import Blueprint, render_template, session, request, Response, jsonify

from datetime import date

from constants.lista_produtos import bebidas as lista_bebidas, doces as lista_doces

from constants.layout_estoque import enderecos

from services.contagem_datas import selecionar_contagem_datas_para_carregar

from scripts.salvar_arquivo_contagem_bebidas import salvar_arquivo_contagem_bebidas
from scripts.salvar_arquivo_contagem_doces import salvar_arquivo_contagem_doces
from scripts.salvar_arquivo_contagem_geladeiras import salvar_arquivo_contagem_geladeiras
from scripts.salvar_arquivo_contagem_datas import salvar_arquivo_contagem_datas


from models.contagem_temporaria import ContagemTemporaria
from models.contagens_datas_temporaria import ContagensDatasTemporaria


contagem_bp = Blueprint("contagem", __name__, url_prefix="/contagem")


@contagem_bp.route("/selecionar_contagem", methods=["GET"])
def selecionar_contagem():
    return render_template("contagem/selecionar_contagem.html")


# ======================================================================
#                         CONTAGEM BEBIDAS
# ======================================================================

@contagem_bp.route("/bebidas", methods=["GET"])
def bebidas():
    return render_template("contagem/contagem_bebidas.html", produtos=lista_bebidas)


@contagem_bp.route("/salvar_contagem_bebidas", methods=["POST"])
def salvar_contagem_bebidas():

    usuario_id = session.get("usuario_id")
    
    contagens = []

    for produto in lista_bebidas:
        campo = f"produto_{produto['codigo']}"
        quantidade = request.form.get(campo)

        if not quantidade:
            quantidade = 0

        contagens.append({
            "codigo": produto["codigo"],
            "nome": produto["nome"],
            "quantidade": int(quantidade)
        })

        
    resultado, mensagem, erro = salvar_arquivo_contagem_bebidas(contagens, usuario_id)

    return render_template("salvar_contagem.html", mensagem=mensagem, erro=erro)


@contagem_bp.route("/salvar_contagem_temporaria", methods=["POST"])
def salvar_contagem_temporaria():

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%Y-%m-%d")

    usuario_id = session.get("usuario_id")

    
    codigo_produto = request.form.get("produto_id")
    quantidade = request.form.get("quantidade")

    if not quantidade:
        quantidade = 0

    nova_contagem = ContagemTemporaria(
        data_atual_formatada,
        usuario_id,
        codigo_produto,
        quantidade
        )
        
    nova_contagem.inserir_contagem()

    return Response(status=204)


@contagem_bp.route("/carregar_contagem_temporaia", methods=["GET"])
def carregar_contagem_temporaria():

    data_atual = date.today()
    data_atual_formatada = data_atual.strftime("%Y-%m-%d")

    usuario_id = session.get("usuario_id")

    if not usuario_id or not data_atual_formatada:
        return jsonify([])

    dados = ContagemTemporaria.carregar_contagem(usuario_id, data_atual_formatada)

    return jsonify(dados)


# ======================================================================
#                         CONTAGEM DOCES
# ======================================================================

@contagem_bp.route("/doces", methods=["GET"])
def doces():
    return render_template("contagem/contagem_doces.html", produtos=lista_doces)


@contagem_bp.route("/salvar_contagem_doces", methods=["POST"])
def salvar_contagem_doces():

    usuario_id = session.get("usuario_id")
    

    contagens = []

    for produto in lista_doces:
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


# ======================================================================
#                      CONTAGEM GELADEIRAS
# ======================================================================

@contagem_bp.route("/geladeiras", methods=["GET"])
def geladeiras():
    return render_template("contagem/contagem_geladeiras.html")


@contagem_bp.route("/salvar_contagem_geladeiras", methods=["GET", "POST"])
def salvar_contagem_geladeiras():

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

    resultado, mensagem, erro = salvar_arquivo_contagem_geladeiras(contagens, usuario_id)

    return jsonify({"status": "ok"})


# ======================================================================
#                      CONTAGEM DATAS
# ======================================================================

@contagem_bp.route("/datas", methods=["GET"])
def datas():

    usuario_id = session.get("usuario_id")

    contagem_a_carregar = selecionar_contagem_datas_para_carregar(usuario_id)

    return render_template(
        "contagem/contagem_datas.html",
        layout_estoque=enderecos,
        contagem_anterior=contagem_a_carregar,
        lista_produtos=lista_bebidas
        )


@contagem_bp.route("/salvar_contagem_datas", methods=["POST"])
def salvar_contagem_datas():

    usuario_id = session.get("usuario_id")

    id = request.form.getlist('id[]')
    ruas = request.form.getlist('rua[]')
    blocos = request.form.getlist('bloco[]')
    colunas = request.form.getlist('coluna[]')
    niveis = request.form.getlist('nivel[]')
    produtos = request.form.getlist('produto[]')
    data_fabricacao = request.form.getlist('data_fabricacao[]')
    data_validade = request.form.getlist('data_validade[]')
    quantidade = request.form.getlist('quantidade[]')

    produtos_dict = {
        str(produto["codigo"]): produto["nome"]
        for produto in lista_bebidas
    }

    contagens = []
    for (
        id,
        rua,
        bloco,
        coluna,
        nivel,
        codigo,
        data_fabricacao,
        data_validade,
        quantidade,
    ) in zip(
        id,
        ruas,
        blocos,
        colunas,
        niveis,
        produtos,
        data_fabricacao,
        data_validade,
        quantidade,
    ):

        contagens.append({
            "id": id,
            "rua": rua,
            "bloco": bloco,
            "coluna": coluna,
            "nivel": nivel,
            "codigo_produto": codigo,
            "nome": produtos_dict.get(codigo),
            "data_fabricacao": data_fabricacao,
            "data_validade": data_validade,
            "quantidade": quantidade
        })

    resultado, mensagem, erro = salvar_arquivo_contagem_datas(contagens, usuario_id)

    return render_template("salvar_contagem.html", mensagem=mensagem, erro=erro)


@contagem_bp.route("/salvar_contagem_datas_temporaria", methods=["POST"])
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
    quantidade = request.form.get('quantidade')


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
        data_validade,
        quantidade
    )

    return Response(status=204)
