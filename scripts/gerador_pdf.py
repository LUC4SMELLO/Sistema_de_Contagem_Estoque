from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.units import cm

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
            c.drawString(posicao_x + 470, posicao_y, i)
            posicao_y -= 20
        

def gerar_relatorio_geladeiras_pdf(lista_equipamentos):

    c = canvas.Canvas(CAMINHO_SAIDA_ARQUIVO, pagesize=A4)  # A4 pagesize
    

    img = ImageReader("static/images/cabeçalho.png")
    img_width, img_height = img.getSize()
    c.drawImage(img, 0, 780, img_width, img_height)


    c.setFont("Helvetica-Bold", 20)
    c.drawString(150, 805, "Relatório Equipamentos")

    c.setFont("Helvetica-Bold", 18)
    c.drawString(10, 752, "Equipamentos:")


    c.setStrokeColorRGB(0.0, 0.0, 0.0) # COR PRETA 
    c.setLineWidth(2) # LARGURA DA LINHA EM PONTOS

    c.line(0, 745, 800, 745)
        


    c.setFont("Helvetica-Bold", 15)
    desenhar_equipamentos(c, lista_equipamentos)

    # FINALIZANDO
    c.showPage()

    # SALVANDO O PDF
    c.save()


gerar_relatorio_geladeiras_pdf(lista_equipamentos)