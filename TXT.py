from datetime import datetime


def salvar_em_txt(dados, nome_arquivo="Resultados/resultados.txt"):
    if not dados:
        print("Nenhum dado para salvar.")
        return

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo: # abre o arquivo para escrita, se não existir ele cria um novo
        arquivo.write("Resultados da Pesquisa - Cases de Agente de IA\n") # escrevo o cabeçalho

        data_atual = datetime.now().strftime("%d/%m/%Y")  # obtendo a data atual
        arquivo.write(f"Data: {data_atual}\n\n") # escrevo a data atual no arquivo

        for atual, item in enumerate(dados, start=1): # obtenho os dados da lista
            titulo = item.get("Título", "Sem título")
            url = item.get("URL", "Sem URL")
            fonte = item.get("Fonte", "Sem fonte")
            resumo = item.get("Resumo", "Sem resumo")

            # escrevo os dados no arquivo
            arquivo.write(f"Resultado número {atual}:\n\n")
            arquivo.write(f"TÍTULO: {titulo}\n")
            arquivo.write(f"URL: {url}\n")
            arquivo.write(f"FONTE: {fonte}\n")
            if resumo:
                arquivo.write(f"RESUMO: {resumo}\n")

            arquivo.write("\n" + "=" * 100 + "\n\n")  # adiciona uma separação entre os resultados

    print(f"Arquivo TXT salvo como {nome_arquivo}")
