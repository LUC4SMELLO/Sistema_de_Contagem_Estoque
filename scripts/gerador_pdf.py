from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from reportlab.lib.pagesizes import A4
from datetime import datetime

CAMINHO_SAIDA_ARQUIVO = "arquivos/contagem_geladeira.pdf"

lista_equipamentos = [
    "GESP785511", "GESP747741", "GESP965511", "GESP362514", 
    "GESP488221", "GESP912547", "GESP332122", "GESP748559", 
    "GESP523344", "GESP980123", "GESP741852", "GESP963214", 
    "GESP123465", "GESP741963", "GESP852741", "GESP369258", 
    "GESP741258", "GESP987654", "GESP654987", "GESP159753", 
    "GESP753159", "GESP456789", "GESP321654", "GESP852369", 
    "GESP159753", "GESP654321", "GESP123789", "GESP456321", 
    "GESP963852", "GESP741852", "GESP852963", "GESP123456", 
    "GESP369258", "GESP258147", "GESP951753", "GESP123789",
    "GESP258963", "GESP321987", "GESP654321", "GESP789456",
    "GESP785511", "GESP747741", "GESP965511", "GESP362514", 
    "GESP488221", "GESP912547", "GESP332122", "GESP748559", 
    "GESP523344", "GESP980123", "GESP741852", "GESP963214", 
    "GESP123465", "GESP741963", "GESP852741", "GESP369258", 
    "GESP741258", "GESP987654", "GESP654987", "GESP159753", 
    "GESP753159", "GESP456789", "GESP321654", "GESP852369", 
    "GESP159753", "GESP654321", "GESP123789", "GESP456321", 
    "GESP963852", "GESP741852", "GESP852963", "GESP123456", 
    "GESP369258", "GESP258147", "GESP951753", "GESP123789",
    "GESP258963", "GESP321987", "GESP654321", "GESP789456",
    "GESP963852", "GESP741852", "GESP852963", "GESP123456", 
    "GESP369258", "GESP258147", "GESP951753", "GESP123789",
    "GESP258963", "GESP321987", "GESP654321", "GESP789456", 
]



def desenhar_equipamentos(c, lista_equipamentos):

    posicao_x = 10
    posicao_y = 720


    # LISTA MENOR QUE 36
    if len(lista_equipamentos) < 36:
        
        for i in lista_equipamentos[:36]:
            c.drawString(posicao_x, posicao_y, i)
            posicao_y -= 20


    # LISTA MAIOR QUE 36 E MENOR QUE 72
    if len(lista_equipamentos) > 36 and len(lista_equipamentos) < 72:

        for i in lista_equipamentos[:36]:
            c.drawString(posicao_x, posicao_y, i)
            posicao_y -= 20

        posicao_x = 10
        posicao_y = 720

        for i in lista_equipamentos[36:72]:
            c.drawString(posicao_x + 240, posicao_y, i)
            posicao_y -= 20


    # LISTA MAIOR QUE 76
    if len(lista_equipamentos) > 76:

        for i in lista_equipamentos[:36]:
            c.drawString(posicao_x, posicao_y, i)
            posicao_y -= 20

        posicao_x = 10
        posicao_y = 720

        for i in lista_equipamentos[36:72]:
            c.drawString(posicao_x + 240, posicao_y, i)
            posicao_y -= 20

        posicao_x = 10
        posicao_y = 720

        for i in lista_equipamentos[72:108]:
            c.drawString(posicao_x + 480, posicao_y, i)
            posicao_y -= 20
        

def gerar_relatorio_geladeiras_pdf(lista_equipamentos, nome_usuario):

    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y - %H:%M")


    c = canvas.Canvas(CAMINHO_SAIDA_ARQUIVO, pagesize=A4)  # A4
    

    img = ImageReader("static/images/cabeçalho.png")
    img_width, img_height = img.getSize()
    c.drawImage(img, 0, 770, img_width, img_height)


    c.setFont("Helvetica-Bold", 20)
    c.drawString(135, 805, "Relatório Equipamentos")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(415, 805, "Usuário: " + str(nome_usuario))

    c.setFont("Helvetica", 10)
    c.drawString(415, 790, str(data_formatada))

    c.setFont("Helvetica-Bold", 18)
    c.drawString(10, 752, "Patrimônios:")


    c.setStrokeColorRGB(0.0, 0.0, 0.0) # COR PRETA 
    c.setLineWidth(2) # LARGURA DA LINHA EM PONTOS


    c.line(180, 730, 180, 20)
    c.line(410, 730, 410, 20)
        


    c.setFont("Helvetica-Bold", 15)
    desenhar_equipamentos(c, lista_equipamentos)

    # FINALIZANDO
    c.showPage()

    # SALVANDO O PDF
    c.save()
