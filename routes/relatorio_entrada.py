from flask import Blueprint, render_template, request

from scripts.ler_arquivo_xml import ler_varios_arquivos_xml, retornar_numeros_das_cargas


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada", methods=["GET", "POST"])
def relatorio_entrada():

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

            itens = request.form.getlist("item[]")
            numero_carga = carga_selecionada
            notas_fiscais = request.form.getlist("nota_fiscal[]")
            codigos_produtos = request.form.getlist("codigo_produto[]")
            descricoes = request.form.getlist("descricao[]")
            fabricacoes = request.form.getlist("fabricacao[]")
            vencimentos = request.form.getlist("vencimento[]")
            observacoes = request.form.getlist("obs[]")

            # CHECKBOXES MARCADOS
            fefo = set(request.form.getlist("fefo[]"))
            pallet_danificado = set(request.form.getlist("pallet_danificado[]"))
            vazamento = set(request.form.getlist("vazamento[]"))

            relatorio = []

            for item, nota_fiscal, codigo_produto, descricao, fabricacao, vencimento, obs in zip(
                itens,
                notas_fiscais,
                codigos_produtos,
                descricoes,
                fabricacoes,
                vencimentos,
                observacoes
            ):

                relatorio.append({
                    "numero_carga": numero_carga,
                    "nota_fiscal": nota_fiscal,
                    "item": item,
                    "codigo_produto": codigo_produto,
                    "descricao": descricao,
                    "fabricacao": fabricacao,
                    "vencimento": vencimento,
                    "fefo": codigo_produto in fefo,
                    "pallet_danificado": codigo_produto in pallet_danificado,
                    "vazamento": codigo_produto in vazamento,
                    "observacao": obs
                })

            for item in relatorio:
                print(item)

            # BANCO DE DADOS


    return render_template(
        "relatorio_entrada.html",
        cargas=cargas,
        notas=dados,
        carga_selecionada=carga_selecionada,
        total_itens=total_itens
    )
