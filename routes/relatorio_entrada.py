from flask import Blueprint, render_template, request, session, Response, jsonify

from scripts.ler_arquivo_xml import ler_varios_arquivos_xml, retornar_numeros_das_cargas

from scripts.salvar_relatorio_entrada import salvar_relatorio_entrada

from services.relatorio_entrada import buscar_relatorios_inseridos, buscar_relatorio_entrada

from models.relatorios_entradas_temporarios import RelatoriosEntradasTemporarios


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__, url_prefix="/relatorio_entrada")


@relatorio_entrada_bp.route("/relatorio_entrada", methods=["GET", "POST"])
def relatorio_entrada():
    return render_template("relatorio_entrada/relatorio_entrada.html",)


@relatorio_entrada_bp.route("/preencher", methods=["GET", "POST"])
def preencher():

    usuario_id = session.get("usuario_id")

    cargas = retornar_numeros_das_cargas()

    dados = None
    carga_selecionada = None
    total_itens = 0

    if request.method == "POST":

        acao = request.form.get("acao")
        carga_selecionada = request.form.get("carga")

        # CARREGA OS DADOS PARA EXIBIÇÃO
        if carga_selecionada:
            dados = ler_varios_arquivos_xml(carga_selecionada)
            total_itens = sum(len(nota["itens"]) for nota in dados)

        # SALVAR RELATÓRIO
        if acao == "salvar":

            motoristas = request.form.getlist("motorista[]")
            locais = request.form.getlist("local[]")

            itens = request.form.getlist("item[]")
            numero_carga = carga_selecionada
            notas_fiscais = request.form.getlist("nota_fiscal[]")
            codigos_produtos = request.form.getlist("codigo_produto[]")
            descricoes = request.form.getlist("descricao[]")
            quantidades = request.form.getlist("quantidade[]")
            fabricacoes = request.form.getlist("fabricacao[]")
            vencimentos = request.form.getlist("vencimento[]")
            observacoes = request.form.getlist("obs[]")

            # CHECKBOXES MARCADOS
            fefo = set(request.form.getlist("fefo[]"))
            pallet_danificado = set(request.form.getlist("pallet_danificado[]"))
            vazamento = set(request.form.getlist("vazamento[]"))

            relatorio = []

            for item, motorista, local, nota_fiscal, codigo_produto, descricao, quantidade, fabricacao, vencimento, obs in zip(
                itens,
                motoristas,
                locais,
                notas_fiscais,
                codigos_produtos,
                descricoes,
                quantidades,
                fabricacoes,
                vencimentos,
                observacoes
            ):

                relatorio.append({
                    "numero_carga": numero_carga,
                    "nota_fiscal": nota_fiscal,
                    "motorista": motorista,
                    "local": local,
                    "item": item,
                    "codigo_produto": codigo_produto,
                    "descricao": descricao,
                    "quantidade": int(float(quantidade)),
                    "data_fabricacao": fabricacao,
                    "data_vencimento": vencimento,
                    "fefo": codigo_produto in fefo,
                    "pallet_danificado": codigo_produto in pallet_danificado,
                    "vazamento": codigo_produto in vazamento,
                    "observacao": obs
                })

            resultado, mensagem, erro = salvar_relatorio_entrada(relatorio, usuario_id)

            return render_template("salvar_contagem.html", mensagem=mensagem, erro=erro)

    return render_template(
        "relatorio_entrada/preencher_relatorio_entrada.html",
        cargas=cargas,
        notas=dados,
        carga_selecionada=carga_selecionada,
        total_itens=total_itens
    )


@relatorio_entrada_bp.route("/visualizar", methods=["GET", "POST"])
def visualizar():

    cargas = buscar_relatorios_inseridos()
    carga_selecionada = None

    if request.method == "POST":

        acao = request.form.get("acao")

        if acao == "buscar":

            carga = request.form.get("carga")

            carga_selecionada, relatorio = buscar_relatorio_entrada(carga)
            
            return render_template("relatorio_entrada/visualizar_relatorio_entrada.html", cargas=cargas, dados_produtos=relatorio, carga_selecionada=carga_selecionada)
        
    return render_template("relatorio_entrada/visualizar_relatorio_entrada.html", cargas=cargas, dados_produtos="", carga_selecionada=carga_selecionada)


@relatorio_entrada_bp.route("/salvar_relatorio_entrada_temporario", methods=["POST"])
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


@relatorio_entrada_bp.route("/carregar_relatorio_entrada_temporario")
def carregar_relatorio_entrada_temporario():
    usuario_id = session.get("usuario_id")

    dados = RelatoriosEntradasTemporarios.buscar_relatorio_temporarios(usuario_id)

    return jsonify(dados)
