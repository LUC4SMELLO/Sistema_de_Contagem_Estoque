from flask import Blueprint, render_template, request, session

from scripts.ler_arquivo_xml import ler_varios_arquivos_xml, retornar_numeros_das_cargas

from scripts.salvar_relatorio_entrada import salvar_relatorio_entrada


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada", methods=["GET", "POST"])
def relatorio_entrada():

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
                    "fabricacao": fabricacao,
                    "vencimento": vencimento,
                    "fefo": codigo_produto in fefo,
                    "pallet_danificado": codigo_produto in pallet_danificado,
                    "vazamento": codigo_produto in vazamento,
                    "observacao": obs
                })


            # BANCO DE DADOS


            resultado, mensagem, erro = salvar_relatorio_entrada(relatorio, usuario_id)


            return render_template("salvar_contagem.html", mensagem=mensagem, erro=erro)


    return render_template(
        "relatorio_entrada.html",
        cargas=cargas,
        notas=dados,
        carga_selecionada=carga_selecionada,
        total_itens=total_itens
    )
