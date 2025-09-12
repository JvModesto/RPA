from openpyxl.styles import Font
from datetime import datetime
from openpyxl.workbook import Workbook

# acabei optando em não usar a biblioteca do pandas, pois assim fica mais fácil de formatar,
# como colocar em negrito e etc. Mas com pandas seria uma excelente alternativa também.
def salvar_em_excel(dados, nome_arquivo="Resultados/resultados.xlsx"):
    if not dados:
        print("Nenhum dado para salvar.")
        return

    data_atual = datetime.now().strftime("%d-%m-%Y") # excel não aceita / no nome do arquivo, então troquei por -

    wb = Workbook()  # cria uma nova planilha
    ws = wb.active # selecionando a planilha criada
    ws.title = "Resultados do dia " + data_atual

    # definir cabeçalhos
    cabeçalhos = ["Número", "Título", "URL", "Fonte", "Resumo"]
    ws.append(cabeçalhos) # função append para adicionar os cabeçalhos na primeira linha da planilha

    # negrito nos cabeçalhos
    for caracter in ws[1]: # a primeira linha da planilha
        caracter.font = Font(bold=True)

    # adicionar os resultados à planilha
    for atual, item in enumerate(dados, start=1):
        titulo = item.get("Título", "Sem título")
        url = item.get("URL", "Sem URL")
        fonte = item.get("Fonte", "Sem fonte")
        resumo = item.get("Resumo", "Sem resumo")

        ws.append([atual, titulo, url, fonte, resumo]) # adiciona os dados na planilha

    # largura das colunas
    for coluna in ws.columns:
        maximo = max(len(str(cell.value)) for cell in coluna if cell.value) # mede o comprimento do maior valor de cada coluna
        # esse calculo é feito para evitar que o excel mostre celulas cortadas ou estreitas.
        ws.column_dimensions[coluna[0].column_letter].width = maximo + 2  # ajusta largura da coluna com um espaço extra

    # salvar o arquivo
    wb.save(nome_arquivo)
    print(f"Arquivo Excel salvo como {nome_arquivo}")