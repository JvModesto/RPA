import csv
from datetime import datetime

def salvar_em_csv(dados, nome_arquivo="Resultados/resultados.csv"):
    if not dados:
        print("Nenhum dado para salvar.")
        return

    # esse with abre o arquivo csv para escrita, se o arquivo não existir ele cria um novo
    with open(nome_arquivo, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo) # cria um objeto escritor para escrever no arquivo
        escritor.writerow(["Número", "Título", "URL", "Fonte", "Resumo", "Data da Pesquisa"])  # cabeçalho do csv
        data_atual = datetime.now().strftime("%d/%m/%Y")  # obtendo a data atual

        for atual, item in enumerate(dados, start=1):
            titulo = item.get("Título", "Sem título")
            url = item.get("URL", "Sem URL")
            fonte = item.get("Fonte", "Sem fonte")
            resumo = item.get("Resumo", "Sem resumo")

            escritor.writerow([atual, titulo, url, fonte, resumo, data_atual])  # escreve a linha no arquivo csv

    print(f"Arquivo CSV salvo como {nome_arquivo}")
