from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas
from datetime import datetime



## cria um pdf com os resultados coletados.
def salvar_em_pdf(dados, nome_arquivo="Resultados/resultados.pdf"):
    data_atual = datetime.now().strftime("%d/%m/%Y")  # obtendo a data atual

    if not dados:
        print("Não há dados para salvar no pdf.")
        return

    pdf = canvas.Canvas(nome_arquivo, pagesize=A4) # cria um novo canvas do ReportLab que será o pdf

    # formatação do pdf: (no reportlab, 1 ponto = 1/72 polegada)
    largura, altura = A4
    margem = 40 # pontos
    y = altura - margem
    linha_altura = 14 # diferença entre as linhas (pontos)

    # cabeçalho do pdf:
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(margem, y, "Resultados da Pesquisa - Cases de Agente de IA")
    y-= linha_altura
    pdf.setFont("Helvetica", 10)
    pdf.drawString(margem, y, f"Data da pesquisa: {data_atual}")  # adiciona a data ao pdf
    y -= 30

    # colocando os resultados no pdf
    for nresultado, item in enumerate(dados, start=1):  # enumerando os resultados
        if y < 100:  # se o espaço estiver acabando, cria uma nova página
            pdf.showPage() # cria a nova página
            y = altura - margem
            pdf.setFont("Helvetica", 10)

        # pega as informações do dicionário item (se não existir, coloca vazio)
        titulo = item.get("Título", "")
        url = item.get("URL", "")
        resumo = item.get("Resumo", "")
        fonte = item.get("Fonte", "")

        # necessário para evitar que o texto ultrapasse os limites do pdf, utilizando a função simpleSplit do ReportLab.
        resumo_lim = simpleSplit(resumo, "Helvetica", 10, largura - 2 * margem)

        # adiciona a numeração dos resultados
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(margem, y, f"Resultado número {nresultado}")
        y -= linha_altura

        pdf.setFont("Helvetica", 10)

        pdf.drawString(margem, y, f"Título: {titulo}") # escrevo o título
        y -= linha_altura

        pdf.drawString(margem, y, "URL: ")
        pdf.setFillColor(blue)  # define a cor azul
        pdf.drawString(margem + 25, y, "Link") # escrevo o Link
        pdf.linkURL(url, (margem + 25, y, margem + 80, y + 14), relative=1)  # torna "Link" clicável no pdf
        # relative=1 faz com que as coordenadas do link sejam relativas à posição atual do canvas (útil se houve translate ou transformações).        y -= linha_altura

        pdf.setFillColor(black)  # volta a cor para preto

        pdf.drawString(margem, y, f"Fonte: {fonte}") # escrevo a fonte
        y -= linha_altura

        if resumo:
            pdf.drawString(margem, y, "Resumo:")
            y -= linha_altura
            for linha in resumo_lim: # como o resumo pode ter sido splittado, coloco um for para escrever cada linha
                pdf.drawString(margem + 20, y, linha)
                y -= linha_altura

        y -= 20  # espaço para o próximo bloco

    pdf.save()
    print(f"Arquivo PDF salvo como {nome_arquivo}")
