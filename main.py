import navegador
import PDF
import TXT
import CSV
import EXCEL

def menu():
    print("\nBem-vindo ao sistema de armazenamento de resultados! Tema da pesquisa: 'cases de agente de IA'")
    limite = int(input("Primeiro, digite quantos resultados você deseja coletar (Mínimo 20): "))
    while limite < 20:
        limite = int(input("O número mínimo de resultados é 20. Tente novamente: "))

    driver = navegador.iniciar_navegador(headless=False)  # abre o navegador
    navegador.buscar_no_google(driver, "cases de agente de IA")  # faz a pesquisa
    resultados = navegador.extrair_resultados(driver, limite)  # extrai os resultados
    driver.quit()  # fecha o navegador no final

    while True:
        print("\nAgora escolha uma opção:")
        print("1) Salvar em TXT")
        print("2) Salvar em PDF")
        print("3) Salvar em CSV")
        print("4) Salvar em EXCEL")
        print("5) Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            TXT.salvar_em_txt(resultados)

        elif escolha == "2":
            PDF.salvar_em_pdf(resultados)

        elif escolha == "3":
            CSV.salvar_em_csv(resultados)

        elif escolha == "4":
            EXCEL.salvar_em_excel(resultados)

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")



menu() # exibe o menu