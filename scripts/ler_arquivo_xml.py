import re
from datetime import datetime
from collections import defaultdict
from pathlib import Path

import xml.etree.ElementTree as ET

from constants.paths import IMPORTS


def ler_arquivo_xml(caminho_xml):

    padrao = r"^.*?(?P<carga>\d+)_(?P<nota_fiscal>\d+)_(?P<motorista>[^_]+)_(?P<placa>[A-Z0-9]+)_(?P<local>[^_]+).*\.xml$"
    resultado = re.match(padrao, str(caminho_xml))

    if resultado:
        dados = resultado.groupdict()


    tree = ET.parse(caminho_xml)
    root = tree.getroot()

    # DICIONÁRIO DE NAMESPACE OBRIGATÓRIO PARA O SEFAZ
    ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

    # IDENTIFICAÇÃO E CHAVE DE ACESSO
    infNFe = root.find(".//nfe:infNFe", ns)
    chave_acesso = infNFe.attrib["Id"].replace("NFe", "") if infNFe is not None else "Não encontrada"
    numero_nota = root.find(".//nfe:ide/nfe:nNF", ns).text
    data_emissao = root.find(".//nfe:ide/nfe:dhEmi", ns).text

    dt = datetime.fromisoformat(data_emissao)
    data_formatada = dt.strftime("%d/%m/%Y %H:%M:%S")

    # DADOS DO EMITENTE E DESTINATÁRIO
    emit_nome = root.find(".//nfe:emit/nfe:xNome", ns).text
    emit_cnpj = root.find(".//nfe:emit/nfe:CNPJ", ns).text
    dest_nome = root.find(".//nfe:dest/nfe:xNome", ns).text
    dest_cnpj = root.find(".//nfe:dest/nfe:CNPJ", ns).text

    # LISTA DE ITENS
    itens = []
    for det in root.findall(".//nfe:det", ns):
        item_num = det.attrib["nItem"]
        
        # DADOS DOS PRODUTOS
        prod = det.find("nfe:prod", ns)
        codigo = prod.find("nfe:cProd", ns).text
        nome = prod.find("nfe:xProd", ns).text
        qtd = prod.find("nfe:qCom", ns).text
        valor_total_prod = prod.find("nfe:vProd", ns).text

        # DADOS DE IMPOSTOS DO ITEM (PIS E COFINS)
        pis = det.find(".//nfe:PIS//nfe:vPIS", ns)
        cofins = det.find(".//nfe:COFINS//nfe:vCOFINS", ns)
        
        v_pis = pis.text if pis is not None else "0.00"
        v_cofins = cofins.text if cofins is not None else "0.00"
    

        item = {
            "item": item_num,
            "codigo":codigo,
            "descricao": nome,
            "quantidade": qtd,
            "valor_total": valor_total_prod,
            "pis": v_pis,
            "cofins": v_cofins
        }

        itens.append(item)

    # DICIONÁRIO FINAL
    nota = {
        "motorista": dados["motorista"],
        "placa": dados["placa"],
        "local": dados["local"],
        "chave_acesso": chave_acesso,
        "numero_nota": numero_nota,
        "data_emissao": data_formatada,
        "emitente": {
            "nome": emit_nome,
            "cnpj": emit_cnpj,
        },
        "destinatario": {
            "nome": dest_nome,
            "cnpj": dest_cnpj,
        },
        "itens": itens,
    }

    return nota


def ler_varios_arquivos_xml(numero_carga):

    notas = {}
    pasta = IMPORTS
    for arquivo in pasta.glob(f"{numero_carga}*.xml"):
        nota = ler_arquivo_xml(arquivo)

        numero = nota["numero_nota"]

        if numero not in notas:
            notas[numero] = nota
        else:
            # JUNTA APENAS OS ITENS
            notas[numero]["itens"].extend(nota["itens"])

    lista_notas = list(notas.values())

    return lista_notas
